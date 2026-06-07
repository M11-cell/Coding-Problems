#include "trafficlight.hpp"
#include <iostream>
#include <thread>
#include <chrono> 

TrafficLight::TrafficLight() : state(TrafficLightState::RED) {}


std::string TrafficLight::to_string(TrafficLightState state) const{
    switch(state){
        case TrafficLightState::RED:
            return "RED";
        case TrafficLightState::YELLOW:
            return "YELLOW";
        case TrafficLightState::GREEN:
            return "GREEN"; 
    }
    return ""; 
}

TrafficLightState TrafficLight::cycle(){
    if(state == TrafficLightState::RED){
        state = TrafficLightState::GREEN;
    } else if(state == TrafficLightState::GREEN){
        state = TrafficLightState::YELLOW;
    } else {
        state = TrafficLightState::RED;
    }

    return state;
}

TrafficLightState TrafficLight::getState() const {
    return state; 
}

// int main(){

//     TrafficLight light; 
//     TrafficLightState state = light.getState(); 
//     while(true){

//         std::cout << "The light is currently: " << light.to_string(state) << std::endl; 
//         std::this_thread::sleep_for(std::chrono::milliseconds(5000)); 
//         state = light.cycle(); 
        
//     }

//     return 0; 
// }