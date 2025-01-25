# wordgame.py (c) Kingsley Ezenwaka k3z3nw4k4@gmail.com
# 2025.01.24

# Import required libraries
from random import randint

# Create a variable to hold the name of the game
gname = "\'GUESS THE WORD\' Game"

# Create word-bank variable
word_bank = []

# Read in words from a word bank file
with open('words.txt', 'r') as word_bank_file:
    for line in word_bank_file:
        word_bank.append(line.rstrip().lower())

# The next line is just to view the full list of words and not needed for gameplay. Comment out before shipping.
# print(word_bank)

# Randomly select the target word to be guessed
tword = word_bank[(randint(0,len(word_bank)-1))]

# The next line is just to view the target word and not needed for gameplay. Comment out before shipping.
# print(tword)

# Define some variables to keep track of game info and gameplay
misplaced_guesses = []
wrong_guesses = []
turns = 0
max_turns = 7

# Gameplay starts here with the welcome statement
print(f"!!Welcome to the {gname}!!\n\nIn this game the computer chooses a 5-letter random word and you have to guess the letters!\nYou will have just {max_turns} turns to guess the letters correctly, so guess wisely!!\n")

# Run the game loop
while True:
    result = []
    guess = input("Guess a 5-letter word...")
    turns += 1

    # Checks if the guessed word is acceptable
    if not (guess.isalpha() and len(guess)==len(tword)): 
        print(f'This entry is not acceptable. Please enter a 5-letter word with no symbols or numbers.')
    else:
        guess = guess.lower()

        # Compares the guessed to target word and gives info to player
        for i in range(0,len(tword)):
            char = guess[i]
            if char == tword[i]:
                result.append(char.upper())
                if char in misplaced_guesses:
                    misplaced_guesses.remove(char)
            else:
                result.append("_")
                if char in tword and char not in misplaced_guesses:
                        misplaced_guesses.append(guess[i])
                else: 
                    if char not in wrong_guesses:
                        wrong_guesses.append(guess[i])
        
        # Shows current game state
        print("Your current game state:")
        print(f"These letters are not in the word at all: {wrong_guesses}")
        print(f"These letters are in the word but misplaced: {misplaced_guesses}")
        print(f"Correct guesses:{result}")

    # Continues or ends gameplay based on conditions
    if guess == tword:
        print(f'\nYou guessed the correct word! It is {tword.upper()}!')
        break
    elif turns < max_turns:
        print(f'\nYou have {max_turns-turns} tries left!\n')
    else:
        print(f'\nYou have exhausted your tries. The word is {tword.upper()}. Better luck next time!')
        break