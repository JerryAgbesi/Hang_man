#A simple Hangman game built using a list.
import random

#Choosing the difficulty level.
#Difficulty level determines number of lives to be given
difficulty = input("choose the level of difficulty(type 1,2 or 3):\n 1.Easy \n 2.normal \n 3.Hard ")
lives = 0


#A list to hold the secret words for the game
secret_words=['freight','instant','blast','admire','advance','marine','bounty','infinite','ruthless','heavenly','purse','diamond']
#Making a random choice from the list of words
current_word = random.choice(secret_words)

board = []
index = 0

#Setting up the board by replacing unknown words with '?'s
while index < len(current_word):
    board.append('?')
    index += 1

#Heart characters to represent number of lives  
heart = u'\u2764'
correct_guess = False

#Storing the number of words in the current mystery word
unknown_letters = len(current_word)

#Function to update the board and update the number of unknown letters in the game

def update_clue(guessed_letter,current_word,board,unknown_letters):
    index= 0
    while index < len(current_word):

        if guessed_letter == current_word[index]:
            board[index] = guessed_letter
            unknown_letters = unknown_letters - 1
        index = index + 1
    return unknown_letters

# Main Game logic
try :# code to make sure user enters the right character
    difficulty = int(difficulty)
    if difficulty == 1:
        lives = 9
    elif difficulty == 2:
        lives = 7
    elif difficulty == 3:
        lives = 3

    while lives > 0: #keeping count of the number of lives left
        print(board)
        print(f'lives left: {heart*lives} ')
        guess = input("guess the word or a letter in the word:")

    #checking if the guesssed word is same as the mystery word
        if guess == current_word:
         correct_guess = True
         break
        #checking for guessed letters in the mystery word
        if guess in current_word:
            unknown_letters = update_clue(guess,current_word,board,unknown_letters)
    #implementing the loss of a life anytime a worng guess is made        
        if guess not in current_word:
            print("incorrect,sorry you lose a life")
            lives -= 1

        if unknown_letters == 0:
            correct_guess = True
            break
    
    #Checking to declare if player won or not
    if correct_guess :
        print(f'congratulations you won!!. The secret word was {current_word}')
    elif correct_guess == False:
            print("you lost,the secret word was"+ ' ' + current_word)
except ValueError:
    print("You entered a wrong chracter")
                    


