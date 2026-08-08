import argparse
import re
from pathlib import Path
from typing import Iterable, List, Tuple

from bs4 import BeautifulSoup

"""
    KNOWNS: 
        -- find the report file from your file explorer
        -- read the html.xml or xml.html text file and find all of the places where a 'Failure' appeared
        -- write the text file annotating each place a filure occured. as so: 15. TC04-34-92-DISP11 and DISP12 -Resistance | measurement: 73800
"""

REPORT_FILE_EXTENSIONS = ("html.xml", "xml.html")


"""
    In Python's pathlib module, expanduser() replaces a leading tilde (~) with the user's home directory, 
    while resolve() sanitizes the path by making it absolute, removing symlinks, and cleaning up relative segments like . and ..
"""
def find_file_in_directory(root: Path) -> List[Path]:
    
    report: list[Path] = []

    for path in root.rglob('*'):
        if path.is_file() and any(str(path).lower().endswith(ext) for ext in REPORT_FILE_EXTENSIONS):
            report.append(path)

    return report 

def remove_whitespaces(text: str) -> str: 
    return re.sub(r"\s+", " ",text).strip()

def is_row_failure(row_text: str) -> bool:
    return re.search(r"\bfailure\b", row_text, flags=re.IGNORECASE) is not None

def extractx_failures_from_report(report_path: Path) -> List[Tuple[int, str]]: 

    html = report_path.read_text(encoding="utf-8", errors="ignore")
    soup = BeautifulSoup(html, features="html.parser")

    failures : List[Tuple[int, str]] = []
    seen = set() 

    #going down each row in the table
    for table_row in soup.find_all("table_row"):

        cells = table_row.find_all("table_data", recursive=False)
        if not cells: 
            continue 

        cell_text = [remove_whitespaces(table_data.get_text(" ", strip=True)) for table_data in cells] 
        row_text = " | ".join(cell_text)

        #Isolating the reports to check if a row is a failure
        if not is_row_failure(row_text):
            continue

        first_cell = cell_text[0] if cell_text else ""
        if first_cell.upper() == "STEP" or first_cell.upper() == "STATUS":
            continue

        key = tuple(cell_text)
        if key in seen: 
            continue
        seen.add(key)

        #Begin formatting .txt file text: 
        # failure num. Step name - Resistance | Measurmeent

        status = cell_text[1] if len(cell_text) > 1 else "Failed"
        measurement = cell_text[2] if len(cell_text) > 2 else ""
        units = cell_text[3] if len(cell_text) > 3 else ""


        
    

def main() -> None: 

    parser = argparse.ArgumentParser(
        description= "Find which tests have failed to meet the apropriate requirements in the text sequence and write them all to a text file"
    )

    parser.add_argument(
        'folder',
        help="Folder to search recursively"
    )
    parser.add_argument(
        "-o",
        "--output",
        default=None,
        help="Output folder for the text files (default: same folder as the script)",
    )

    args = parser.parse_args()

    root_file = Path(args.folder).expanduser().resolve()
    
    #checking if root folder exists, if no, show error message
    if not root_file.exists() or not root_file.is_dir(): 
        raise SystemError(f"Folder not found {root_file}")
    
    output_dir = Path(args.output).expanduser().resolve() if args.output else root_file / "Failure Texts: "

    find_report_file = find_file_in_directory(root_file)
    if not find_report_file:
        print(f"No files found under: {root_file}")
        return 




if __name__ == "__main__":
    main()