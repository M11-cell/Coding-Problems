#include "Atomic_mass.hpp"


//The function molectume_mass takes in an arbitrary number of arguments of element symbols as strings respresenting a molecule
// and returns the molectule as a single string where each element is separated by an '_' character and the molecules atomic mass. 


//Helper function here helps take care of removing the '-' in the elements if there is one.

std::pair<std::string, int> splitDash(const std::string& element){
    size_t dashPos = element.find('-'); 

    if(dashPos != std::string::npos){ 

        std::string elementName = element.substr(0, dashPos);//Here were adding the first element of the string into the vecotr
        int elementSize = std::stoi(element.substr(dashPos+1)); //Here were adding the number after the '-' into the vector
        return {elementName, elementSize}; 
    }
    else{
        return {element, 1};
    }

}

std::pair<std::string, int> molecule_mass(const std::vector<std::string>& molecule_stwing){

    int element_mass = 0;
    int element_sum = 0; 
    std::string new_element = "";


    //TODO: combine the elements together w/ a '_'
    //TODO: Multiply the elements by their respective atomic mass & sum them up. 
    for(std::string s : molecule_stwing){
        std::pair<std::string, int> element = splitDash(s); 
        new_element += s + "_";
        element_mass = element.second*periodic_table[element.first]; 
        element_sum += element_mass; 
    } 
    

    return {new_element.substr(0, new_element.size()-1), element_sum}; 
}


int main(){

    std::vector<std::string> molecules = {"C-6", "H-12"}; 
    std::pair<std::string, int> result = molecule_mass(molecules);
    
    std::cout<< "The completed molecule and its mass are: " << result.first << ", " << result.second << std::endl;
    return 0; 
}


/*

    LESSONS LEARNT:

    VECOTRS CAN ONLY STORE ONE DATA TYPE, NOT TWO!!!

    - you can access different vecotr indeces by simply doing v[index_num]; 

    - .substr() extracts a portion of a string, starting at a specified position and extending for a 
        given number of characters (start, length)

    - npos is a constant static memeber set to -1. If npos returns -1, then the character in the string you are looking for is 
        likely not there. (So you alwyas want to check if your variable is != std::string::npos)

    - std::stoi conversts strings into integer value. 

    - if you want to store/return two different data types then use std::pair !

    - angle brackets (<>) are used for STANDARD LIBRARIES HEADERS whereas "" are for USER-DEFINED/LOCAL HEADERS



*/