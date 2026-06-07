#include "car.hpp"
#include <iostream>
#include <string>


/*
    Use constructor bodies when you need to perform actual operations, validity checks, and stuff like that. 
    An aggregate like this doesn't need any of that. In that case yeah, that's a good place to use this. 
    However you may also have an alternative: member construction functions. 
    For the example i'm making up a class where the constructor has a reason for exist, 
    in this class you want variables to only be positive values.

*/

Car::Car(std::string carid, std::string direction_, int speed) 
    : carID(std::move(carid)), direction{std::move(direction_)}, speed(speed) {} 

    

void Car::move(){

    std::cout << "A " << carID << " is moving " << direction << std::endl;
}



