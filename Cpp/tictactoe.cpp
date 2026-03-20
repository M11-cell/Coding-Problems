#include <iostream>
#include <string>

using namespace std;


class Player{

    public:
        Player(char sym = 'X', string n = "Player X") : symbol(sym), name(n){}

        char getSymbol() const {return symbol;}
        string getName() const {return name;}

    private:

        char symbol; 
        string name; 
};

class GameBoard{

    public:
        //Using the constructor1 to initialize the board
        GameBoard() : counter(0){
            
            //i represents columns, j represents rows. 
            for(int i = 0; i < 3; i++){
                for(int j = 0; j < 3; j++){
                    grid[i][j] = ' ';
                }
            }
        }

        void drawBoard() const{
            cout<<"-------------" << endl;
            for(int i = 0; i<3; i++){
                cout<< "| ";
                for(int j = 0; j < 3; j++){
                    cout << grid[i][j] << " | "; 
                }
                cout<< endl << "-------------" << endl; 
            }
        }
        
        //Method that checks if the move was valid
        bool isValidMove(int row, int col) const{
            return (row >=0 && row < 3 && col >= 0 && col < 3 && grid[row][col] == ' '); 
        }

        // method to make a move
        void makeMove(int row, int col, char Symbol) {

                if(isValidMove(row, col)){
                    grid[row][col] = Symbol; 
                    counter++; //incrementing the counter when cell is filled
                }
        }

        //check wins: check diagonals, columns, and rows
        bool checkWin(char Symbol) const{
            
            //checking rows
            for(int i = 0; i < 3; i++){
                if(grid[i][0] == Symbol && grid[i][1] == Symbol && grid[i][2] == Symbol){
                    return true; 
                }
            }
            
            //checking columns
            for(int i =0; i<3;i++){
                if(grid[0][i] == Symbol && grid[1][i] == Symbol && grid[2][i] == Symbol){
                    return true; 
                }
            }

            //checking diagonals
            if(grid[0][0] == Symbol && grid[1][1] == Symbol && grid[2][2] == Symbol){
                return true;
            }
            if(grid[0][2] == Symbol && grid[1][1] == Symbol && grid[2][0] == Symbol){
                return true;
            }

            return false; 

        }
        
        //check to see if board is full 
        bool isFull() const{
            
            return counter == 9; 
            
        }

        int getFilledCells() const{
            return counter; 
        }

    private: 

        char grid[3][3]; 
        int counter;  // counter for filled cells
};

//handles overall game logic: player turns, processes user input, checks win/draw conditions. 
class TictacToe{

    public: 
        TictacToe() : currentPlayerIndex(0){
            players[0] = Player(); //reduces redundancy since default value is already set in constructor. 
            players[1] = Player('O', "Player O"); 
        }

        //Function to get current player
        Player& getCurrentPLayer() {
            return players[currentPlayerIndex]; 
        }

        //Method to switch turns
        void switchTurn() {
            currentPlayerIndex = (currentPlayerIndex +1)%2; 
        }

        //method to play the game
        void play(){

            int row, col; 
            cout << "Welcome to Tic-Tac-Toe!" << endl; 

            while(!board.isFull()){

                board.drawBoard(); 

                Player& currentplayer = getCurrentPLayer(); 

                while(1){
                    
                    cout<< currentplayer.getName() << " (" << currentplayer.getSymbol() 
                        << "), enter row (1-3) and column (1-3): ";
                    cin >> row >> col; 
                    row--; col--; //convert to 0-indexed. 
                    
                    if(board.isValidMove(row, col)){
                        break;
                    }else{
                        cout<< "invalid move, please try again" << endl;
                    }
                }

                board.makeMove(row, col, currentplayer.getSymbol());
                    
                //Check for da win 
                if(board.checkWin(currentplayer.getSymbol())){
                    board.drawBoard();
                    cout << currentplayer.getName() << " Wins !" << endl;
                    return;
                }
                
                switchTurn(); 

            }

            //game ended in draw
            board.drawBoard();
            cout<< "its a draw!" << endl; 
        }

         
    
    private:

        GameBoard board; 
        Player players[2]; 
        int currentPlayerIndex; 

};

int main(){

    TictacToe game;

    game.play();
    return 0; 
}