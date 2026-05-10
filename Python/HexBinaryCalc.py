
HEX_TO_BIN: dict = {
    "0":"0000", "1":"0001", "2":"0010", "3":"0011",
    "4":"0100", "5":"0101", "6":"0110", "7":"0111",
    "8":"1000", "9":"1100", "A":"1001", "B":"1010",
    "C":"1011", "D":"1100", "E":"1110", "F":"1111"
}


def convertHexToBinary(hexInput: str) -> str:
    ... 

def convertBinaryToHex(BinaryInput: str) -> str:
    ... 

def isvalidateHex(string: str) -> bool:
    ... 

def isvalidBinary(string: str) -> bool: 
    
    if string == "":
        return False
    
    return all(c in ('0', '1') for c in string)

def getConversionDirection() -> str:
    
    print("======= Hex/Binary Converter =======")
    choice: str = input("Please input desired conversion (hex/binary):\n\n")

    choice = choice.lower() # Note: Strings in python are IMMUTABLE (can not be modified in place aka. simply doing choice.lower() is incorrect)

    while choice not in ('hex', 'binary'):
        choice = input("Invalid conversion type, please try again:\n\n")
        choice = choice.lower()

    return choice

def main():
    
    try:
        
        direction: str = getConversionDirection()
        result: str = ""
        userInput: str = ""

        if direction == 'hex':
            userInput = input("Enter a Binary value:    ")

            while not isvalidBinary(userInput):
                userInput = input("Invalid binary input, please try again:\n\n")
            
            result = convertBinaryToHex()
            print(f"Binary value: {userInput} \n Hex value: {result}")

        else:

            userInput = input("Enter a Hex value:   ")

            while not isvalidateHex(userInput):
                userInput = input("Invalid hex input, please try again:\n\n")

            result = convertHexToBinary()
            print(f"Hex value: {userInput} \n Binary value: {result}")

    except (ValueError, TypeError) as e:
        print("Error: ", e)


if __name__ == "__main__":
    main()