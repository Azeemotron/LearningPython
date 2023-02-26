# Day 2 - Exercise 1: Data Types
# Exercise Completed & Checked via Coding Rooms Submission Checker

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

#  The inputed data will be in the format of a string

firstNumber = two_digit_number[0]  # We use the square bracket to specify we want the 1st character
secondNumber = two_digit_number[1]  # We use the square bracket to specify we want the 2nd character

print(int(firstNumber) + int(secondNumber))  # Strings can't do arithmetic operations, so we convert them

#  Sometimes an easy mistake to make, remember to print things, otherwise console will not display anything
