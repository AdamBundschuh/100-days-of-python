#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

TEMPLATE_PATH = "./Input/Letters/starting_letter.txt"
SAVE_PATH = "./Output/ReadyToSend/"

with open("./Input/Names/invited_names.txt", "r") as data:
    names = data.readlines()

for name in names:
    recipient_name = name.strip()
    with open(TEMPLATE_PATH, "r") as data:
        new_letter = data.read().replace("[name]", recipient_name)

    file_name = "letter_to_" + recipient_name.replace(" ", "_") + ".txt"
    with open(SAVE_PATH + file_name, mode="w") as data:
        data.write(new_letter)

