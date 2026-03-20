#include <cstdlib>
#include <ctime>
#include <iostream>

char getComputerResponse(){

    int move;

    //generating numbers between 1 and 2
    srand(time(NULL));
    move = rand() % 3;

    if(move == 0) return 'R';
    if (move == 1) return 'P';
    return 'S'; 
}

int getResult(char playerMove, char computerMove){

    if(playerMove == computerMove) return 0; 

    if(playerMove == 'R' && computerMove == 'S') return 1; 

    if(playerMove == 'S' && computerMove == 'P') return 1; 

    if(playerMove == 'P' && computerMove == 'R') return 1; 

    if(computerMove == 'R' && playerMove == 'S') return -1; 

    if(computerMove == 'S' && playerMove == 'P') return -1; 

    if(computerMove == 'P' && playerMove == 'R') return -1; 

    return 0; 
}


int main(){

    std::cout<< "Welocome to the Rock Paper Scissors game ! " << '\n';

    char playerMove;
    while(playerMove != 'q'){
         std::cout<< "Please Select either; 'R' for rock, 'P' for paper, and 'S' for scissors" << std::endl; 
        while(1){
            std::cin >> playerMove;
            if(playerMove == 'q'){
                exit(0); 
            }
            if(playerMove == 'R' || playerMove == 'P' || playerMove == 'S'){
                break;
            }else{
                std::cerr << "Invalid move, please try again";  
            }
        }

        char computerMove =  getComputerResponse(); 
        

        int result = getResult(playerMove, computerMove); 

        if(result == 0){
            std::cout << "Game draw" << std::endl;
        }

        if(result == 1){
            std::cout << "Congrats! You win ! " << std::endl; 
        }

        if(result == -1){
            std::cout << "Womp womp, you lose" << std::endl; 
        }

        std::cout << "Your move: " << playerMove << '\n';
        std::cout << "Computer Move: " << computerMove << '\n'; 
    }

    return 0; 
}
