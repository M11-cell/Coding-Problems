//Check for da win 
                if(board.checkWin(currentplayer.getSymbol())){
                    board.drawBoard();
                    cout << currentplayer.getName() << " Wins !" << endl;
                    return;
                }
                
                switchTurn(); 