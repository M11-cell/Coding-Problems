#include <iostream> 
#include <vector> 
#include <cmath>
#include <map>

std::map<int, std::string> RomanToInt = {
    {1, "I"}, {5, "V"}, {10, "X"}, {50, "L"}, {100, "C"}, {500, "D"}, {1000, "M"}
};


int main(){

    int num = 4949;
    std::vector<int> number_list; 
    std::string result = ""; 

    while(num > 0){

        int digit = num % 10; 
        number_list.push_back(digit);
        num /= 10; 
    }

    for(size_t i{}; i < number_list.size(); ++i){
        
        int multiplier = pow(10, i);

        int res = number_list[i] * multiplier;

        if(res == 4 || res == 9){

            res+= 1;
            result = RomanToInt.at(res);
            result.insert(0, RomanToInt.at(1));
            std::cout << result;
            
        }else if(res == 40 || res == 90){
            
            res+= 10;
            result = RomanToInt.at(res);
            result.insert(0, RomanToInt.at(10));
            std::cout << result;

        }else if(res == 400 || res == 900){

            res+= 100;
            result = RomanToInt.at(res);
            result.insert(0, RomanToInt.at(100));
            std::cout << result;
        }else{

            
        }
    }

    return 0; 
}