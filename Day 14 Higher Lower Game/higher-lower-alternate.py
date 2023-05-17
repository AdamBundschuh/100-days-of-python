from art import *
from game_data import data
from random import choice
from os import system
system('cls')

def format_data(account):
    '''Takes the account data and returns the printable format.'''
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

print(logo)
score = 0

account_b = choice(data)

game_should_continue = True
while game_should_continue:

    account_a = account_b
    account_b = choice(data)
    while account_a == account_b:
        account_b = choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Agaisnt B: {format_data(account_b)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_follower_count = int(account_a["follower_count"])
    b_follower_count = int(account_b["follower_count"])

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    system('cls')
    print(logo)

    if is_correct:
        score += 1
        print(f"Correct. Current score: {score}")
    else:
        print(f"Wrong. Final score {score}")
        game_should_continue = False