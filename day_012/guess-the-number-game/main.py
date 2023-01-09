#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo
#Print Welcome message
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
#Pick random number from 1-100
cpu_guess = random.randint(1, 100)
print(f"Pssst, the correct answer is {cpu_guess}")

# Include easy mode hard mode
guesses = 0
mode = input("Choose a difficulty. Type 'easy' or 'hard': ")
if mode == "easy":
    guesses = 10
elif mode == "hard":
    guesses = 5
print(f"You have {guesses} attempts remaining to guess the number.")
#Ask user for a guess
#player_guess = int(input("Make a guess: "))
#print(player_guess)

def game():
    player_guess = int(input("Make a guess: "))
    global guesses
    if player_guess > cpu_guess:
        print("Too high.")
        #return guesses -= 1
        guesses -= 1
        print(f"You have {guesses} attempts remaining to guess the number.")
    elif player_guess < cpu_guess:
        print("Too low.")
        #return guesses -= 1
        guesses -= 1
        print(f"You have {guesses} attempts remaining to guess the number.")
    elif player_guess == cpu_guess:
        print(f"Yay! {player_guess} is the Correct Answer. \n Game Over!")
        #return guesses = 0
        guesses = 0
        


while guesses > 0:
    game()

print(f"You have {guesses} attempts remaining to guess the number. \n Game Over!" )
#Still do do each loop of game reduce guess
#when all guess used end game