# {key: Value}

test_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A peice of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
    "Error": "I.D. 10-T error."
}

#Retrieving items from dictionary.
print(test_dictionary["Bug"])

#Adding items to dictionary.
test_dictionary["Variable"] = "A variable used in a program."
print(test_dictionary)

empty_dictionary = {}

#Wipe existing dictionary
# test_dictionary = {}
# print("Dictionary wiped.")
# print(test_dictionary)

#Edit an item in a dictionary.
test_dictionary["Bug"] = "A moth in your computer."
print(test_dictionary)

#Loop through a dictionary.
for key in test_dictionary:
    print(key)
    print(test_dictionary[key])