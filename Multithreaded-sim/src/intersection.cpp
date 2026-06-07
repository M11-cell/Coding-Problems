#include "intersection.hpp"
#include <algorithm>

void Intersection::addLane(const Lane& lane){
     lanes.push_back(lane);
} 

void Intersection::addLight(const TrafficLight& light){
     lights.push_back(light); 
}

bool Intersection::passagepriority(const Car& car) const{
     return car.isEmergency();
}

void Intersection::update() {

     //Should let give priority to emergency vehicles, allowing them to pass thru da intersection 
     // Should update the lanes (max 3 lanes * 4 streets) each time a new thread joins 

     const std::size_t count = std::min(lanes.size(), lights.size());

     for(size_t i = 0; i < count; i++){

          switch(lights[i].getState()){
               case TrafficLightState::RED:
                    return; 

               case TrafficLightState::YELLOW:

                    return; 

               case TrafficLightState::GREEN:

                    return ;
               }

          }

}
     

/*

     Intersection Design; 

          1. Should check the state of the light. 

               If the light is red, civilian cars should stay stopped and not move until the light turns green 
               If the light is red, emergency vehicles can go right through, but vehicles in other threads NEED to be stopped. 
          
          2. There should be a maximum of 3 lanes/ road => 12 lanes total. 

          3. the intersection should have 4 roads 

*/