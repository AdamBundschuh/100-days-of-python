############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from art import logo
import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def get_player_score():
    return sum(player_cards)

def get_dealer_score():
    return sum(dealer_cards)

def starting_hands():
    player_cards.clear()
    dealer_cards.clear()
    for _ in range(0,2):
        player_hit()
        dealer_hit()

def player_hit():
    card = random.choice(cards)
    if card == 11 and get_player_score() > 10:
        card = 1
    player_cards.append(card)

def display_player_score():
    print(f"Your cards: {player_cards}, current score: {get_player_score()}")

def dealer_hit():
    card = random.choice(cards)
    if card == 11 and get_dealer_score() > 10:
        card = 1
    dealer_cards.append(card)

def display_dealer_score():
    print(f"Computer's first card: {dealer_cards[0]}")

player_cards = []
dealer_cards = []

def blackjack():

    os.system('cls')
    print(logo)

    starting_hands()
    display_player_score()
    display_dealer_score()

    another_turn = True
    player_busted = False
    dealer_busted = False

    # Players Turn
    while another_turn:
        choice = input(f"\nType 'y' to get another card, type 'n' to stand: ").lower()
        os.system('cls')
        if choice == 'y':
            player_hit()
            if get_player_score() > 21:
                player_busted = True
                break
            else:
                display_player_score()
                display_dealer_score()
        else:
            break

    # Dealers Turn
    while get_dealer_score() <= 17 and not player_busted:
        dealer_hit()
        if get_dealer_score() > 21:
            dealer_busted = True

    print(f"Your final hand: {player_cards}, final score: {get_player_score()}")
    print(f"Dealer final score: {get_dealer_score()}\n")

    # End of game message
    if player_busted:
        print("You busted, you lose.")
    elif dealer_busted:
        print("Dealer busted, you win!")
    elif get_player_score() == 21 and get_dealer_score() != 21:
        print("Blackjack! You win!")    
    elif get_player_score() > get_dealer_score():
        print("You win!")
    elif get_dealer_score() > get_player_score():
        print("You lose.")    
    else:
        print("It's a draw, house wins.")

    # Play another game prompt
    another_game = input("\nWould you like to play again? 'y' or 'n': ").lower()
    if another_game == 'y':
        blackjack()

os.system('cls')
start = input("Do you want to play a game of Blackjack? 'y' or 'n': ").lower()
if start == 'y':    
    blackjack()
elif start == 'n':
    print("Ok, bye loser.")
else:
    print("You can't type, bye.")