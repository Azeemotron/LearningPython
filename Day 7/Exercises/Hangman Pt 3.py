# Step 3

import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
playerWinStatus = False  # This is how we'll check if the player has won or not to close the loop.

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

# So the trick here is to wrap a bunch of code into a While Loop so it can repeat until the player wins.

while playerWinStatus == False:
    guess = input("Guess a letter: ").lower()

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(display)

    if "_" not in display:
        playerWinStatus = True  # Ends the loop, marks that the player has won.
        print("You Win.")
