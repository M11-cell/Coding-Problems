#include <iostream>
#include <string>
#include <cctype>


int main(){

    std::string s;
    std::cout<< "Input a word: ";
    std::cin >> s; 

    std::string result; 

    for(int i = 0; i < s.size(); i++)
    {
        result += std::tolower(s[i]);

    }
    

    std::cout<< "lower cased word is: " << result << '\n'; 

    int left = 0; 
    int right = s.size() - 1; 

    while(left < right)
    {
        if(result[left] != result[right])
        {
            std::cout<< "This word is not a palindrome";
            return 0;
        }

        left++;
        right--;
    }

    std::cout<< "This word is a palindrome"; 
    return 1; 
}