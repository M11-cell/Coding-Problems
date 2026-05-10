import random 
import string


"""
Hangman: 

    - Pick a random word

    - Player needs to guess that word in a certain number of attempts before losing the game


"""


class Hangman:

    def __init__(self):
        self.secretWord = self.getRandomWord()
        self.CurrentWord = '_' * len(self.secretWord)
        self.guessedLetters = []
        self.attempsLeft = 6 

    def play(self):
        
        self.drawHangman()
        while self.attempsLeft > 0:

            self.displayGameInfo()
            print("Guess a letter: ")
            guess = input() 

            if guess.isalpha():

                if guess.isupper():
                    guess = guess.lower() 
                    #Now check if guess was correct
                if self.alreadyGuessed(guess):
                    print("You've already guessed that letter")
                else:
                    correctGuess = self.updateCurrentWord(guess)

                    if correctGuess: 
                        print("Nice guess!")
                        self.drawHangman()
                    
                        if self.CurrentWord == self.secretWord:
                            self.displayGameInfo()
                            print("CONGRATS ! You guessed the secret word: ", self.secretWord)
                            return 
                        
                    else:
                        self.attempsLeft -= 1
                        self.drawHangman()

            else:

                print("Please type in a letter")

            if self.attempsLeft == 1:
                print("sheeeeee, you lost mate, try again next time. The word was: ", self.secretWord)
                return 
                

    
    def getRandomWord(self) -> string:

        word = ["Hello", "petal", "Mommy", "Peanut", "Canada", "Argentina", "blossom", "airplane", "example", "calculus", "python", "computer", "goat"]
        
        return random.choice(word)

    def alreadyGuessed(self, letter) -> bool:
        #needs fixing
        return letter in self.guessedLetters
    
    def updateCurrentWord(self, letter) -> bool:
        
        correctGuess = False 
        #needs fixing
        for i in range(len(self.secretWord)):
            
            if self.secretWord[i] == letter:
                self.CurrentWord = self.CurrentWord[:i] + letter + self.CurrentWord[i + 1:]
                correctGuess = True


        self.guessedLetters.append(letter)
        return correctGuess

    def displayGameInfo(self):
        
        print("Word: ", self.CurrentWord)
        print("Attempts Left: ", self.attempsLeft)
        print("Guessed Letters: ", ", ".join(self.guessedLetters))
    

    def drawHangman(self):

        if(self.attempsLeft == 6):
            print(" _____")
            print(" |    |")
            print(" |     ")
            print(" |     ")
            print(" |.    ")
            print(" |.    ")
            print(" |     ")
            print("----   ")

        if(self.attempsLeft == 5):
            print(" _____")
            print(" |    |")
            print(" |    O")
            print(" |     ")
            print(" |.    ")
            print(" |.    ")
            print(" |     ")
            print("----   ")

        if(self.attempsLeft == 4):
            print(" _____")
            print(" |    |")
            print(" |    O")
            print(" |    |")
            print(" |.    ")
            print(" |.    ")
            print(" |     ")
            print("----   ")
        if(self.attempsLeft == 3):
            print(" _____")
            print(" |    |")
            print(" |    O")
            print(" |    |")
            print(" |.   |")
            print(" |.    ")
            print(" |     ")
            print("----   ")
        if(self.attempsLeft == 2):
            print(" _____")
            print(" |    |")
            print(" |    O")
            print(" |    |")
            print(" |.   |")
            print(" |.  / ")
            print(" |     ")
            print("----   ")
        if(self.attempsLeft == 1):
            print(" _____")
            print(" |    |")
            print(" |    O")
            print(" |    |")
            print(" |.   |")
            print(" |.  / \\")
            print(" |     ")
            print("----   ")
        if(self.attempsLeft == 0):
            print(" _____")
            print(" |    |")
            print(" |    O")
            print(" |    |")
            print(" |.   |")
            print(" |.  /^\\")
            print(" |     ")
            print("----   ")


def main():

    Hangman().play()

if __name__ == "__main__":
    main()