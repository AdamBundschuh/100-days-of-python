from art import *
from game_data import data
from random import choice
from os import system
system('cls')

def get_new_data():
    return choice(data)


def print_data(data, type):
    name = data['name']
    desc = data['description']
    country = data['country']
    print(f"Compare {type}: {name}, a {desc}, from {country}.")


def get_answer(a_data, b_data):
    '''Compares "A Data" and "B Data" to determine which has the highest follower count, returns "a" or "b"'''
    return 'a' if a_data['follower_count'] > b_data['follower_count'] else 'b'


def compare_guess(answer, guess, current_score, high_score):
    '''Compares the followers and checks against the guess, returns the current and high scores.'''
    system('cls')
    if guess == answer:
        current_score += 1
        high_score += 1
        print(f"You're right! Current score: {current_score}")
        return current_score, high_score
    else:
        current_score = 0
        print(f"Sorry, that's wrong. Final score: {high_score}\n")
        return current_score, high_score


def game():  

    a_data = get_new_data()
    b_data = get_new_data()

    current_score = 0
    high_score = 0
    
    next_round = True
    while next_round:
        # Get new "B Data" if it's the same as "A"
        while a_data == b_data:
            b_data = get_new_data()

        print(logo)
        print_data(a_data, 'A')
        print(vs)
        print_data(b_data, 'B')

        answer = get_answer(a_data, b_data)
        #print(f"\nPssst, the answer is '{answer.upper()}'")
        guess = input("\nWho has more followers? Type 'A' or 'B': ").lower()
                
        current_score, high_score = compare_guess(answer, guess, current_score, high_score)

        # If compare_guess returns 0, guess was incorrect, exit game
        if current_score == 0:
            next_round = False
            break
        
        # Update a_data to correct guess
        if answer == 'b':
            a_data = b_data

        # Get new b_data
        b_data = get_new_data()


game()
