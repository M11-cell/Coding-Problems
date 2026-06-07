#include <iostream> 
#include <thread>
#include <mutex>
#include <chrono> 


int quick_mafs = 0; 
std::mutex mtx; 

void foo(){

    std::cout<< "Hello World ! - from thread1" << std::endl;
}

int foo2(){


    //Mutexes prevent race conditions from happening cuz it makes it so that only one thread can
    //access a function at a time. 
        std::lock_guard<std::mutex> lock(mtx); 
        
        for(int i = 0; i < 1000000; i++){
            quick_mafs++; 
        }
    
        return quick_mafs; 
}


int main(){

    //Syntax for creating a thread
    std::thread thread1(foo);

    //passing in parameters to a thread
    std::thread thread3(foo2);
    std::thread thread2(foo2); 

    //.join() is used to wait for a thread to finish execution. 
    thread1.join();

    thread3.join();
    thread2.join();     

    std::cout<< "Foo2 = " << quick_mafs << std::endl;
    std::cout<<"Thread1 has finished executing." << std::endl; 

    return 0; 
}   