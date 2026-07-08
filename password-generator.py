import random
import string  # this is for password generator

print("=== Password Generator ===")

length = int(input("Enter password length: "))

letters_choice = input("Include letters? (y/n): ").lower()
numbers_choice = input("Include numbers? (y/n): ").lower()
symbols_choice = input("Include symbols? (y/n): ").lower()

characters = ""

if letters_choice == "y":
    characters += string.ascii_letters

if numbers_choice == "y":
    characters += string.digits

if symbols_choice == "y":
    characters += string.punctuation

if characters == "":
    print("Error: You must choose at least one character type.")
else:
    password = "".join(random.choices(characters, k=length))
    print("\nGenerated Password:", password)