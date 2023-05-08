import os
from art import logo
 
# Clearing the Screen
os.system('cls')

print(logo)
print("Welcome to the secret auction program.")

bids = {}

add_another_bidder = True

while add_another_bidder:
    name = input("What is your name?: ")
    bid = int(input("What's your bid? $"))

    bids[name] = bid

    another_bidder = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
    if another_bidder ==  'no' or another_bidder == 'n':
        add_another_bidder = False

    os.system('cls')

high_bid = 0
winner_name = ''

for name in bids:
    current_bid = int(bids[name])
    if current_bid > high_bid:
        high_bid = current_bid
        winner_name = name

print(f"The winner is {winner_name} with a bid of ${high_bid}")
