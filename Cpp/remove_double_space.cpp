#include <iostream>
#include <cstring>

std::string removeDoubleSpaces(std::string text)
{
    std::string cleaner; 
    bool lastWasSpace = false;
    
        //(:) Range-based for loop to iterate over characters in 'text'
    for(char c : text)
    {
        if(c == ' ')
        {
            if(!lastWasSpace)
                cleaner += c; 
                lastWasSpace = true; 
        }
        else
        {
            cleaner += c; 
            lastWasSpace = false;
        }
    }
    return cleaner; //gives finished string back to main function. 
}

int main()
{
std::string text = "I     like apples and   bananas"; 
    std::string new_text = removeDoubleSpaces(text);
    std::cout<< new_text << '\n';

}