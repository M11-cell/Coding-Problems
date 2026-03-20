#pragma once 


#include <map>
#include <iostream>
#include <vector>
#include <string>


std::map<std::string, int> periodic_table = {
    {"H", 1}, {"He", 4}, {"Li", 7}, {"Be", 9}, {"B", 11},
    {"C", 12}, {"N", 14}, {"O", 16}, {"F", 19}, {"Ne", 20},
    {"Na", 23}, {"Mg", 24}, {"Cl", 35},
}; 


std::pair<std::string, int> molecule_mass(const std::vector<std::string>& molecule_stwing);