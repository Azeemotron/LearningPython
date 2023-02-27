# Day 3 - Exercise 2: BMI Calculator 2.0
# Exercise Completed & Checked via Coding Rooms Submission Checker

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

bmi = round(weight / (height ** 2))  # Use brackets to prioritise Multiplication over Division

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif 18.5 < bmi < 25:  # 'elif' is only used when the previous IF Statement is not True
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif 25 < bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif 30 < bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")
