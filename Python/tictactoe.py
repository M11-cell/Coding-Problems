
#tic tac toe game. 
class Player:
    def __init__(self, name = "Player1", symbol = "X"):
        self.name = name
        self. symbol = symbol
    
    def getName(self):
        return self.name
       
    def getSymbol(self): 
        return self.symbol


class Board:
    def __init__(self):
        self.rows, self.cols = (3,3)
        self.grid = [[' '] * self.cols for _ in range(self.rows)]
        self.grid_count = 0 

    #prunt the board
    def printBoard(self):
        rows = len(self.grid)
        print("----+---+----")
        for i in range(rows):
            print("|", self.grid[i][0], "|", self.grid[i][1], "|", self.grid[i][2], "| ")
            print("----+---+----")
        return self.grid
    
    #check if move is valid
    def isValidMove(self, row, col) -> bool:
        #valid if move is within the bounds of the game and also the move is within the spaces  
        return (0 <= row < self.rows and 0 <= col < self.cols and self.grid[row][col] == ' ')
    
    #make a move 
    def MakeMove(self, row, col, symbol):
        #to make a move, check if move is valid then one must simply place down the X, or O symbol wherever it has been specified
        if self.isValidMove(row, col):
            self.grid[row][col] = symbol
            self.grid_count+=1
    
    #check for win 
    def checkWin(self, symbol) -> bool: 
        
        #checking for diagonals, rows and cols
        for i in range(self.rows):
            if self.grid[i][0] == symbol and self.grid[i][1] == symbol and self.grid[i][2] == symbol:
                return True

        for i in range(self.cols):
            if self.grid[0][i] == symbol and self.grid[1][i] == symbol and self.grid[2][i] == symbol:
                return True

        if self.grid[0][0] == symbol and self.grid[1][1] == symbol and self.grid[2][2] == symbol:
            return True
        if self.grid[0][2] == symbol and self.grid[1][1] == symbol and self.grid[2][0] == symbol:
            return True
        
        return False

    #check to see if grid is full 
    def isFull(self)-> bool:
        return self.grid_count == 9
    
    def getCurrentGridCount(self): 
        return self.grid_count

    
class TicTacToe:
    def __init__(self): 
        self.players = [Player("Player1", "X"), Player("Player2", "O")]
        self.currentPlayerIndex = 0

    def getPlayerIndex(self) -> Player:
        return self.players[self.currentPlayerIndex]
    
    def switchTurns(self):
        self.currentPlayerIndex = (self.currentPlayerIndex + 1) % 2 # always alternates between 0 and 1
    
    def play(self):
        board = Board()
        print("Welcome to the Tic Tac Toe Game !")

        while not board.isFull(): 

            board.printBoard()
            currentPlayer = self.getPlayerIndex()

            while 1: 

                print(currentPlayer.getName(), " (", currentPlayer.getSymbol(), ") ", "Please enter a number from (1-3) for rows and columns")
                try:
                    row = int(input()) - 1 #converting it to index format
                    col = int(input()) - 1
                except ValueError:
                    print("Please enter numbers only.")
                    continue
                

                if board.isValidMove(row, col):
                    break
                else:
                    print("That was an invalid number, please try again :c")

            board.MakeMove(row, col, currentPlayer.getSymbol())

            if(board.checkWin(currentPlayer.getSymbol())):
                board.printBoard()
                print("Congrats ! ", currentPlayer.getName(), "Wins !")
                return None
            
            self.switchTurns()


        board.printBoard()
        print("its a draw!")


        

def main():

    TicTacToe().play()

if __name__ == "__main__":
    main()