# Day 3 - Exercise 4: Pizza Order Practice
# Exercise Completed & Checked via Coding Rooms Submission Checker

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
bill = 0

# Indentation Level Is IMPORTANT In Python
# Rather than the whole thing being a nested IF Statement, It could also simply be 3 separate 'IF' Statements
if size == "S":
    bill += 15
    if add_pepperoni == "Y":  # Indented so only executes if previous 'IF' is True
        bill += 2
    if extra_cheese == "Y":  # Being in-line with previous IF, executes regardless of previous 'IF' Trueness
        bill += 1
elif size == "M":
    bill += 20
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
elif size == "L":  # Changed from 'ELSE' statement
    bill += 25
    if add_pepperoni == "Y":
        bill += 3  # '+=' or '-=' is the same as (in this instance) bill = bill + x
    if extra_cheese == "Y":
        bill += 1

print(f"Your final bill is: ${bill}.")
