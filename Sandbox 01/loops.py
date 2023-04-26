#Password Generator Project 

import random

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", ",", ".", "/", "?", "<", ">"]

print("Welcome to the PyPassword Generator!")
allow_duplicates = input(f"Allow duplicate characters? (Y/N)\n").upper()
allow_duplicates = True if allow_duplicates == "Y" else False

nr_letters = int(input("How many letters would you like in your password?\n"))
while not allow_duplicates and not 1 <= nr_letters <= len(letters):
    nr_letters = int(input(f"How many letters would you like in your password? (1-{len(letters)})\n"))
    
nr_symbols = int(input(f"How many symbols would you like?\n"))
while not allow_duplicates and not 1 <= nr_symbols <= len(symbols):
    nr_symbols = int(input(f"How many symbols would you like? (1-{len(symbols)})\n"))

nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password_as_list = []

for letter in range(1,nr_letters + 1):
  random_num = random.randint(1, len(letters))
  password_as_list.append(letters[random_num - 1])

for symbol in range(1,nr_symbols + 1):
  random_num = random.randint(1, len(symbols))
  password_as_list.append(symbols[random_num - 1])

for number in range(1,nr_numbers + 1):
  random_num = random.randint(1, len(numbers))
  password_as_list.append(numbers[random_num - 1])

password_ordered = "".join(password_as_list)
print(f"Password ordered (with duplicates allowed): {password_ordered}")
  
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

random.shuffle(password_as_list)
password_random = "".join(password_as_list)
print(f"Password randomised (with duplicates allowed): {password_random}")

#Super Hard Level - No Repeat Letters or Symbols (Numbers can repeat):

password_as_list.clear()
selected_random_nums = []

# print(f"Lenght of letters list: {len(letters)}")
# print(f"Lenght of symbols list: {len(symbols)}")
# print(f"Lenght of numbers list: {len(numbers)}")

def get_random_number(listType):
    random_num = random.randint(0, len(listType) - 1)
    return random_num
    
def add_random_character(listType):
    random_num = get_random_number(listType)
    while listType[random_num] in password_as_list and not allow_duplicates:
        random_num = get_random_number(listType)
    password_as_list.append(listType[random_num])

for letter_loop in range(1,nr_letters + 1):
    add_random_character(letters)

for symbol_loop in range(1,nr_symbols + 1):
    add_random_character(symbols)

for number_loop in range(1,nr_numbers + 1):
  random_num = random.randint(1, len(numbers))
  password_as_list.append(numbers[random_num - 1])
    
random.shuffle(password_as_list)
password_random_unique = "".join(password_as_list)
print(f"Password randomised (with duplicates not allowed): {password_random_unique}\n")
