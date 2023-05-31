#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

template = "./Input/Letters/starting_letter.txt"
save_path = "./Output/ReadyToSend/"

names = open("./Input/Names/invited_names.txt", "r")

for name in names:
    recipient_name = name.strip()
    file_name = "letter_to_" + recipient_name.replace(" ", "_").lower() + ".txt"

    with open(template, "r") as data:
        letter = data.read().replace("[name]", recipient_name)

    with open(save_path + file_name, mode="w") as data:
        data.write(letter)

