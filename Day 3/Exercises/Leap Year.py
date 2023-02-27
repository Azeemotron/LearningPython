# Day 3 - Exercise 3: Leap Year
# Exercise Completed & Checked via Coding Rooms Submission Checker

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

if year % 4 == 0:  # By nesting the 'IF' it means the previous 'IF' must be satisfied before moving on
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap Year")
else:
    print("Not leap year.")

# At first, I attempted to incorporate ELIF. ELIF works if the previous IF is NOT True
# With Nested IF, the previous IF MUST be True
