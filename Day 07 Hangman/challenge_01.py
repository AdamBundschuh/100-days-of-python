#Step 1 
import random

word_list = ["monkey", "silverback", "gorilla", "serena"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(word_list)
chosen_word_length = len(chosen_word)

print(f"The random word chosen is {chosen_word}")
# print(word_length)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("Guess a letter: ").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
    

