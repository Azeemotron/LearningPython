# Day 4 - Exercise 2: Banker Roulette
# Exercise Completed & Checked via Coding Rooms Submission Checker

import random  # We can't use the random functions (such as randint) without importing this module first

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

listLength = len(names) - 1  # I have to minus 1 otherwise it becomes 5

personToPay = random.randint(0, listLength)  # Since lists start at 0, it has to be up to 4, not 5
# Another way to do it would be (0, listLength - 1) as opposed to doing it in the variable

print(f"{names[personToPay]} is going to buy the meal today!")  # Square brackets so specify what in the list

# The above code is for educational purposes. 'random.choice(names)' would actually do everything for us
