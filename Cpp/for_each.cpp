#include <algorithm>
#include <iostream>
#include <vector>

namespace functorClass{

    class FunctorClass{

        private:

            //What does this do? This is defensive programming, its not strictly necessary, but since our class holds a reference 
            //member, m_evenCount, and copying references can be problematic, we add it just in case. 

            //Note: operators overload the = or the () in order to control what happens to each operator. 
            FunctorClass& operator = (const FunctorClass&); 
            int& m_evenCount; //m_evenCount directly modifies the evenCount in the constructor? 

        public: 

            
            explicit FunctorClass(int& evenCount) : m_evenCount(evenCount) {}

            void operator()(int n){

                std::cout<< n; 
                if(n % 2 == 0)
                {
                    std::cout<< " is even " << std::endl;
                    m_evenCount++; 
                }else{
                    std::cout << " is odd " << std::endl; 
                }
            }
    };
}


int main(){



    std::vector<int> myVec; 
    for(int i = 1; i < 11; i++){
        myVec.push_back(i); 
    }

    try
    {
        /* code */
        int evenCount = 0;
        std::for_each(myVec.begin(), myVec.end(), functorClass::FunctorClass(evenCount)); 
        std::cout << "There are " << evenCount
        << " even numbers in the vector." << std::endl;
    }
    catch(const std::exception& e)
    {
        std::cerr << e.what() << '\n';
    }
    
    

    return 0; 
}