#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import os
import random
os.system('cls')

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
    '''Checks the answer against the guess, returns the number of turns remaining.'''
    line_break()
    if guess < answer:
        print(f"{guess} is too low.")
        return turns - 1
    elif guess > answer:
        print(f"{guess} is too High.")
        return turns - 1
    else:
        print(f"You got it! The answer is {answer}")

def set_difficulty():
    level = input("Enter difficulty ('easy' or 'hard'): ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
    
def line_break():
    print("----------------------------------------------------")

# GAME START
def game():
    print(logo)

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1,100)
    # print(f"Pssst, the number is {answer}")

    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            line_break()
            print(f"You've ran out of turns, the answer was {answer}.")
            return

game()
