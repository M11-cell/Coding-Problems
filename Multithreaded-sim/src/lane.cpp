#include "lane.hpp"
#include <chrono>

void Lane::addCar(std::shared_ptr<Car> car){

    if(cars.empty()){
        std::cout << "there are currently no cars in the lane" << std::endl;
        return; 
    } 

    cars.emplace(car); 
    std::cout<< car->carID << " has pulled up on Lane " << getSize(); 
       
}

std::shared_ptr<Car> Lane::removeCar(){
    if(cars.empty()){
        return nullptr;
    }
    auto car = std::move(cars.front()); //Note: std::move avoids extra refcount increment. 
    cars.pop(); //Note: .pop() has a VOID return type => you cant actually return cars.pop()!
    return car;
}

int Lane::getSize() const{
    return cars.size(); 
}