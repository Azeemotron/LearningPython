# Day 5 - Create A Password Generator: End Project
# Exercise Completed & Checked Against Solution

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""

for passwordLetters in range(nr_letters):
    selectedCharacter = random.randint(0, len(letters) - 1)  # Easier method would be using random.choice()
    password += letters[selectedCharacter]

for passwordNumbers in range(nr_numbers):
    selectedCharacter = random.randint(0, len(numbers) - 1)
    password += numbers[selectedCharacter]

for passwordSymbols in range(nr_symbols):
    selectedCharacter = random.randint(0, len(symbols) - 1)
    password += symbols[selectedCharacter]

password = ''.join(random.sample(password, len(password)))  # Empty quotes says no separators
print(password)

# The random.sample obtains a characters from the input sting in a randomly
# The second argument for it is the number of times I want it to randomly grab a character
# So in this instance, I want it to do it the length of the password so it's does it all
