#include <algorithm>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <string>
#include <vector>

// Hangman: Have a vector containing random words be picked out of it and have the user make guess on what it could be.
// implement a class called hangman which gets the random words, checks if letter has already been guessed, draws the hangman, and plays the game.
// as well as a display game info and a function to update the current word.

#define MAX_ATTEMPTS 6
using namespace std;

class Hangman
{

public:
    Hangman()
    {

        srand(static_cast<unsigned int>(time(nullptr)));
        secretWord = getRandomWord();
        currentWord = string(secretWord.length(), '_');
        attemptsLeft = MAX_ATTEMPTS;
    }

    void play()
    {
        // Hangman in a nutshell:
        // Blank underscores appear marking the length of the word.
        // You guess a letter. A. you get it right, and the letter gets filled. B. you guess it wrong, you gain a limb and game continues.

        char x;
        cout << "Hello and welcome to the Hangman Game ! Do you wish to play?" << endl;
        cin >> x;
        if (x == 'y')
        {
            cout << "very well then, let us carry on !" << endl;
        }
        else
        {
            exit(0);
        }

        cout << "You have: " << attemptsLeft << " attempts left !" << endl;

        // The game continues until all trys are up, or until word is guessed. is word was guessed incorrectly, update hangman
        drawHangman(attemptsLeft);
        while (attemptsLeft > 0)
        {
            displayGameInfo();
            char guess;
            cout << "guess a letter " << endl;
            cin >> guess;
            
            if(isalpha(guess)){
                guess = tolower(guess); 
                if(alreadyGuessed(guess)){
                    cout<< "youve already guessed that letter" << endl; 
                }else{
                    bool correctGuess = updateCurrentWord(guess);
                    if(correctGuess){
                        cout << "Good Guess !" << endl; 
                        drawHangman(attemptsLeft);

                        if(currentWord == secretWord){
                            displayGameInfo();
                            cout<< "Hooray ! You guessed the word: " << secretWord;
                            return;  
                        }
                    }else{
                        attemptsLeft--; 
                        drawHangman(attemptsLeft);
                    }
                }  
            }else{
                cout<< "please enter a valid letter" << endl; 
            }

            if(attemptsLeft == 1){
                cout<< "The secret word was ... " << secretWord << ". better luck next time" << endl;
                return;
            }
        
        }
    }

private:
    string secretWord;
    string currentWord;
    vector<char> guessedLetters;
    int attemptsLeft;

    string getRandomWord()
    {
        vector<string> words = {"hallelujah", "apple", "banana", "love", "fajita", "dinner", "alessia", "yourmom"};
        int index = rand() % words.size();
        return words[index];
    }

    bool alreadyGuessed(char letter)
    {
        return find(guessedLetters.begin(), guessedLetters.end(), letter) != guessedLetters.end();
    }

    bool updateCurrentWord(char letter)
    {
        bool correctGuess = false;

        for (int i = 0; i < secretWord.length(); i++)
        {
            if (secretWord[i] == letter)
            {
                currentWord[i] = letter;
                correctGuess = true;
            }
        }
        // adding the correct letter into the guessed letters list
        guessedLetters.push_back(letter);
        return correctGuess;
    }

    void displayGameInfo()
    {
        cout << "Word: " << currentWord << endl;
        cout << "Attempts Left: " << attemptsLeft << endl;
        cout << "Guessed Letters; ";
        for (char letter : guessedLetters)
        {
            cout << letter << " ";
        }
        cout << endl;
    }

    void drawHangman(int attemptsLeft)
    {

        if(attemptsLeft == 6){
            cout << " _____" << endl;
            cout << " |    |" << endl;
            cout << " |     " << endl;
            cout << " |     " << endl;
            cout << " |.    " << endl;
            cout << " |.    " << endl;
            cout << " |     " << endl;
            cout << "----   " << endl;
        }
        else if (attemptsLeft == 5)
        {
            cout << " _____" << endl;
            cout << " |    |" << endl;
            cout << " |    O" << endl;
            cout << " |     " << endl;
            cout << " |.    " << endl;
            cout << " |.    " << endl;
            cout << " |     " << endl;
            cout << "----   " << endl;
        }

        else if (attemptsLeft == 4)
        {
            cout << " _____" << endl;
            cout << " |    |" << endl;
            cout << " |    O" << endl;
            cout << " |    |" << endl;
            cout << " |.    " << endl;
            cout << " |.    " << endl;
            cout << " |     " << endl;
            cout << "----   " << endl;
        }
        else if (attemptsLeft == 3)
        {
            cout << " _____" << endl;
            cout << " |    |" << endl;
            cout << " |    O" << endl;
            cout << " |    | " << endl;
            cout << " |.   | " << endl;
            cout << " |.    " << endl;
            cout << " |     " << endl;
            cout << "----   " << endl;
        }

        else if (attemptsLeft == 2)
        {
            cout << " _____" << endl;
            cout << " |    |" << endl;
            cout << " |    O" << endl;
            cout << " |    |" << endl;
            cout << " |.   |" << endl;
            cout << " |.  / " << endl;
            cout << " |     " << endl;
            cout << "----   " << endl;
        }

        else if (attemptsLeft == 1)
        {
            cout << " _____" << endl;
            cout << " |    |" << endl;
            cout << " |    O" << endl;
            cout << " |    | " << endl;
            cout << " |.   | " << endl;
            cout << " |.  / \\" << endl;
            cout << " |     " << endl;
            cout << "----   " << endl;
        }
    }
};

int main()
{

    Hangman hangman;
    hangman.play();

    return 0;
}