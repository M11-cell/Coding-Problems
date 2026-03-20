#include "ceasarcipher.hpp"
#include <array>

namespace ceasarcipher{

    std::string encrypt(std::string word, int rotation_num){

        if(word.size() != 5){
            std::cout << "Invalid stirng, word must be 5 characters rong";
            exit(0);
        }
        
        std::string new_word;
        for(char c : word){
            new_word += wrapperCB(c, rotation_num);  
        }

        return new_word; 

    }



    std::string decrypt(std::string encryption, int rotation){

        if(encryption.size() != 5){
            std::cout << "Invalid stirng, word must be 5 characters rong";
            exit(0);
        }

        
        return encrypt(encryption, -rotation);

    }


    char wrapperCB(char c, int rotate){

        int ascii_char = static_cast<int>(c);

        int new_ascii_char = ascii_char + rotate; 

        if(new_ascii_char > 126){
            new_ascii_char = 42 + (new_ascii_char - 127);
        }

        if(new_ascii_char < 42){
            new_ascii_char = 126 - (41 - new_ascii_char); 
        }

        return static_cast<char>(new_ascii_char); 

    }

} // namespace ceasarcipher

//Todo: To encrypt you must rotate EACH CHARACTER in the string by a fixed number of of positions down its alphanumerical ordering. 
// Example: char = 'a', rotate = 3 --> 'a' + 3 = 'c'

//Todo: decrypt is same as encrypt, just in reverse. 

//Todo: If ascii number reaches 42 on one end, or 126 on the other, you must wrap back the code to the other end.
// ex: 123 + 5 = 128. => we must wrap back to: 123 -> 124 -> 125 -> 126 -> 42 -> 43. 

int main(){

    std::string word = "Hello";
    int rotation = 3;
    auto new_word = ceasarcipher::encrypt(word, rotation); 

    std::cout << "The new word is... " << new_word << std::endl;

    std::cout << "Hmmm, I wonder what this word means... Let's decipher it !";

    std::cout << " \n The deciphered word is.... " << ceasarcipher::decrypt(new_word, rotation) << '\n';
    std::cout <<"Oh ..." << std::endl;

    return 0;
}