#include <iostream>
#include <vector>
#include <string> 
#include <algorithm>

static bool cont = true; 
std::pair<std::vector<char>, bool> rmCommonLetters(std::vector<char> a, std::vector<char> b){

    for(int i = 0; i < a.size(); i++){
        for(int j = 0; j < b.size(); j++){

            if(a[i] == b[j]){

                char c = a[i]; 

                a.erase(std::remove(a.begin(), a.end(), c), a.end());
                b.erase(std::remove(b.begin(), b.end(), c), b.end());

                const std::size_t splitIndex = a.size();
                a.insert(a.end(), b.begin(), b.end());
                a.insert(a.begin() + splitIndex, '-');
                cont = true; 
                
                return {a, cont};
            }
        }
    }
    cont = false; 
    return {a, cont}; 
}


int main(){

    //take in player string and convert it into a character vector
    std::string p1 = "";
    std::string p2 = ""; 

    std::cout << "Player 1 Name: " << std::endl;
    std::cin  >> p1;
    std::cout << "Player 2 Name: " << std::endl;
    std::cin >> p2;  

    //check to see if letters are upper case, if so, convert them to lower. 
    std::vector<char> new_name1;
    std::vector<char> new_name2; 
    for(char c : p1){
        if(isupper(c)){
            char c1 = tolower(c); 
            new_name1.push_back(c1);
        }else{
            new_name1.push_back(c);
        }
    }
    for(char c : p2){
        if(isupper(c)){
            char c2 = tolower(c); 
            new_name1.push_back(c2);
        }else{
            new_name1.push_back(c);
        }
    }


    while(cont){

        std::pair<std::vector<char>, bool> tmp = rmCommonLetters(new_name1, new_name2); 

    }

    return 0 ; 
}