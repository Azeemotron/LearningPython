# Day 4 - Rock Paper Scissors: End Project
# Exercise Completed & Checked Against Solution

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

options = ["Rock", "Paper", "Scissors"]

playerSelection = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

playerChoice = options[playerSelection]

computerChoice = random.choice(options)  # Got to be cautious, this returns a STRING value, not Int

# The confusion I was having and where I have to be careful is that referencing lists return their value
# NOT their position in this list

if playerChoice == "Rock":
    print(rock)
elif playerChoice == "Paper":
    print(paper)
elif playerChoice == "Scissors":
    print(scissors)

if computerChoice == "Rock":
    print(rock)
elif computerChoice == "Paper":
    print(paper)
elif computerChoice == "Scissors":
    print(scissors)

if playerChoice == "Rock" and computerChoice == "Scissors":
    print("You Win")
elif playerChoice == "Paper" and computerChoice == "Rock":
    print("You Win")
elif playerChoice == "Scissors" and computerChoice == "Paper":
    print("You Win")
elif playerChoice == "Scissors" and computerChoice == "Rock":
    print("You Loose")
elif playerChoice == "Paper" and computerChoice == "Scissors":
    print("You Loose")
elif playerChoice == "Rock" and computerChoice == "Paper":
    print("You Loose")
else:  # For all instances not covered
    print("It's a Draw")
