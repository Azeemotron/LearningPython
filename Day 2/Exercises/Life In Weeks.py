# Day 2 - Exercise 3: Life In Weeks
# Exercise Completed & Checked via Coding Rooms Submission Checker

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
lifeLimit = 90

yearsLeft = lifeLimit - int(age)

timeInDays = round(yearsLeft * 365)  # 'round' stops decimal numbers by rounding up
timeInWeeks = round(yearsLeft * 52)
timeInMonths = round(yearsLeft * 12)

print(f"You have {timeInDays} days, {timeInWeeks} weeks, and {timeInMonths} months left.")

# fString is a Formatted String Literal, lets us use curly brackets to input non-string values
