#include <iostream>
#include <string>

//Write a program that checks if the following string is in decreasing ascii order. 
int main(){

    std::string string = "oOC2";
    
    for(int i = string.size() - 1; i > 0; i--){
        
        if(static_cast<int>(string[i]) < static_cast<int>(string[i+1])){

            std::cout<< "This string is NOT in decreasing order";
            return 0; 
        }

    }
    std::cout<< " This string is in decreasing order!";
    return 1; 
}