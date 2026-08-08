#include <iostream> 
#include <vector> 
#include <cmath>
#include <utility>
#include <string>

std::vector<std::pair<int, std::string>> RomanToInt = {{1000, "M"}, {900, "CM"}, {500, "D"}, {400, "CD"}, {100, "C"}, {90, "XC"}, {50, "L"}, {40, "XL"}, {10, "X"}, {9, "IX"}, {5, "V"}, {4, "IV"}, {1, "I"}};



int main(){

    std::string result = ""; 
    int num = 3342;

    for(size_t i{} ; i < RomanToInt.size() ; ++i){
        while(num >= RomanToInt[i].first){
            result += RomanToInt[i].second; 
            num -= RomanToInt[i].first;
        }
    }

    std::cout << result;

    return 0; 
}