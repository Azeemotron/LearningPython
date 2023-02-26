# Day 2 - Exercise 2: BMI Calculator
# Exercise Completed & Checked via Coding Rooms Submission Checker

sHeight = input("Enter Your Height:   ")  # Important to store the input as a variable first
height = float(sHeight)  # Only then can it be converted to a float (using sHeight instead of 'input')

sWeight = input("Enter Your Weight:   ")
weight = float(sWeight)

bmi = weight / height ** 2  # ** Is the Exponent Operator (To The Power Of)

print(int(bmi))  # The exercise requested result as whole number, so we have to convert to int
