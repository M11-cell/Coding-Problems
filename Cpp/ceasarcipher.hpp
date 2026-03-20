#pragma once

#include <iostream>
#include <string>

namespace ceasarcipher{


    std::string encrypt(std::string word, int rotation_num);


    std::string decrypt(std::string encryption, int rotation); 


    char wrapperCB(char c, int rotate); 

} // namespace ceasarcipher