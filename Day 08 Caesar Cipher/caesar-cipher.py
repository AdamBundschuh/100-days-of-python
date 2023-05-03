import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)
run_again = True

while run_again:
    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    if shift > 25:
        shift = shift % 26
    
    def caesar_cipher(text_passed, shift_amount, cipher_direction):
        end_text = ""
        if cipher_direction == "decode":
            shift_amount *= -1
        for char in text_passed:
            if char not in alphabet:
                end_text += char
            else:
                position = alphabet.index(char)
                new_position = position + shift_amount
                end_text += alphabet[new_position]
        
        
        print(f"The {cipher_direction}d text is {end_text}")
        
    caesar_cipher(text_passed=text, shift_amount=shift, cipher_direction=direction)
            
    another = input("Would you like to encode/decode another message? (y/n)\n").lower()
    if another == "n" or another == "no":
        run_again = False
        print("Goodbye")