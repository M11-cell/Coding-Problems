#include <iostream>
#include <map>
#include <string>
#include <algorithm>
#include <stdexcept>
#include <cctype>

// Conversion maps
const std::map<char, std::string> HEX_TO_BIN = {
    {'0', "0000"}, {'1', "0001"}, {'2', "0010"}, {'3', "0011"},
    {'4', "0100"}, {'5', "0101"}, {'6', "0110"}, {'7', "0111"},
    {'8', "1000"}, {'9', "1001"}, {'A', "1010"}, {'B', "1011"},
    {'C', "1100"}, {'D', "1101"}, {'E', "1110"}, {'F', "1111"}
};

//converts hexadecimal string to binary representation
std::string convertHexToBinary(const std::string& hexInput){

    std::string result = ""; 
    /* Note, you could also do this: 

        std::string hexDigits = hexInput.substr(2); (to remove 0x)
        for(char c : hexDigits){

            result += HEX_TO_BIN.at(c)
        }


    */
    for(size_t i = 2; i < hexInput.size(); ++i){
        result += HEX_TO_BIN.at(hexInput[i]);
    }

    return result; 
}

// Converts binary string to hexadecimal representation
std::string convertBinaryToHex(const std::string& binaryInput) {
    
    std::string result = ""; 

    std::string bin = binaryInput;
    int raw = static_cast<int>(bin.size() % 4); 
    //if bin.size %4 != 0, add 2 zeros on left most side
    if(raw != 0)  bin = std::string(4 - raw, '0') + bin; // Or equivalently; bin.insert(0, 4- raw, '0'); 

    for(size_t i = 0; i < bin.size(); i+=4){
        std::string chunk = bin.substr(i, 4);
        int val = std::stoi(chunk, nullptr, 2);
        char hexChar; 
        if (val < 10) hexChar = static_cast<char>('0' + val);
        else hexChar = static_cast<char>('A' + (val - 10));
        result += hexChar; 
    }

    return std::string("0x") + result;
}


// Validates if a string is a valid hexadecimal number (with 0x prefix)
bool isValidHexadecimal(const std::string& input) {
    if (input.length() <= 2) return false;
    if ((input.substr(0, 2) != "0x" && input.substr(0, 2) != "0X")) return false;   // substr() definitiely a worthy function to keep in mind. 
    
    return std::all_of(input.begin() + 2, input.end(),  // all_of is definitely another worthy funtion. 
        [](char c) { return (c >= '0' && c <= '9') || 
                            (c >= 'a' && c <= 'f') || 
                            (c >= 'A' && c <= 'F'); });
}

// Validates if a string contains only binary digits (0 or 1)
bool isValidBinary(const std::string& input) {
    if (input.empty()) return false;
    
    return std::all_of(input.begin(), input.end(),
        [](char c) { return c == '0' || c == '1'; });
}

// Prompts user to select conversion direction
std::string getConversionDirection() {
    std::string choice;
    
    std::cout << "\n=== Hex/Binary Converter ===\n";
    std::cout << "Convert to (hex/binary): ";
    std::cin >> choice;
    
    // Convert to lowercase for case-insensitive comparison
    std::transform(choice.begin(), choice.end(), choice.begin(), ::tolower);
    
    while (choice != "hex" && choice != "binary") {
        std::cout << "Invalid input. Please enter 'hex' or 'binary': ";
        std::cin >> choice;
        std::transform(choice.begin(), choice.end(), choice.begin(), ::tolower);
    }
    
    return choice;
}

int main() {

    try {
        std::string direction = getConversionDirection();
        std::string input;
        std::string result;
        
        if (direction == "hex") {
            // Convert binary to hex
            std::cout << "\nEnter binary value: ";
            std::cin >> input;
            
            while (!isValidBinary(input)) {
                std::cout << "Invalid binary input. Please enter only 0s and 1s: ";
                std::cin >> input;
            }
            
            result = convertBinaryToHex(input);
            std::cout << "\nBinary: " << input << "\nHexadecimal: " << result << "\n";
            
        } else {
            // Convert hex to binary
            std::cout << "\nEnter hexadecimal value (e.g., 0xABCD): ";
            std::cin >> input;
            
            while (!isValidHexadecimal(input)) {
                std::cout << "Invalid hexadecimal input. Please enter with 0x prefix: ";
                std::cin >> input;
            }
            
            result = convertHexToBinary(input);
            std::cout << "\nHexadecimal: " << input << "\nBinary: " << result << "\n";
        }
        
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << "\n";
        return 1; // Note: returning 1 in main signifies that the program has come across an error! But in other functions, returning 1 = true. 
    }
    
    return 0;
}