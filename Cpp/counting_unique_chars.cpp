#include "iostream"
#include <vector> 
#include <string> 

//todo 2: Hace este mismo ejercisio pero con pointers. 

int count_unique_chars(std::string s){

    std::vector<char> seen_chars{}; 
    std::vector<int> count_chars{};  

    for(char c : s){

        bool found = false; 

        for(int i = 0; i < seen_chars.size(); i++){
            
            if (seen_chars[i] == c){

                count_chars[i] ++;
                found = true;
                break; 
            }
        }
        
        // Only add the character if it wasn't found
        if (!found) {
            seen_chars.push_back(c);
            count_chars.push_back(1); 
        }
    }

    int count = 0; 
    for(int i = 0; i < seen_chars.size();i++){
        if (count_chars[i] == 1){
            count++; 
        }
    }
    return count; 

}




int main(){

    std::string some_stwing = "YourMomisSoGay213023";
    int msg = count_unique_chars(some_stwing); 

    std::cout << "This stwing has " << msg << " unique characters" << '\n'; 
    return 0; 
}