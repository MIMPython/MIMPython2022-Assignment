# The alphabet
from asyncio import sleep


alphabet = 'abcdefghijklmnopqrstuvwxyz'

# Function to encrypt a text based on the Rot-13 method
def encrypt(text):
    """The function receives a string as input, and encrypts it using the Rot-13 method """
    
    # Transform the string to lower-case chars
    text = text.lower()
    
    # the encrypted message
    result = ''
    
    # Replace each letter in the string with a letter which is 13 positions further
    for char in text:
        if char.isalpha():
            result += alphabet[(alphabet.index(char) + 13) % 26]
        else:
            result += char
    return result
        


def decrypt():
    
    print("Welcome to Caesar Cipher Decryption.\n")
    encrypted_message = input("Enter the message you would like to decrypt: ").strip()
    print()
    key = int(input("Enter key to decrypt: "))
    
    decrypted_message = ""

    for c in encrypted_message:

        if c in alphabet:
            position = alphabet.find(c)
            new_position = (position - key) % 26
            new_character = alphabet[new_position]
            decrypted_message += new_character
        else:
            decrypted_message += c

    print("\nDecrypting your message...\n")
    sleep(2) # give an appearance of doing something complicated
    print("Stand by, almost finished...\n")
    sleep(2) # more of the same
    print("Your decrypted message is:\n")
    print(decrypted_message)

decrypt()