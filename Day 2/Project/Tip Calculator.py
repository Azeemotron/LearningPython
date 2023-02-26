# Day 2 - Tip Calculator: End Project
# Exercise Completed & Checked Against Solution

# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇

print("Welcome To The Tip Calculator.")

totalBill = float(input("What was the total bill? £"))  # Money should always use float and not int

tipPercentage = (input("What percentage tip would you like to give? 10, 12, or 15? "))
tipPercentage = "1." + tipPercentage  # Calculations will be easier if we put the percentage in this format
# An easier way rather than combining strings, would just be to + 1 to 12 after it's been / 100 (0.12)

splitValue = int(input("How many people to split the bill? "))

costPerPerson = (totalBill / splitValue) * float(tipPercentage)  # We can now turn the string into a float. BIDMAS
# Another way to round this could be to: round(costPerPerson, 2)

print(f"Each Person Should Pay: £{costPerPerson:.2f}")  # F String formatting used ':.2f' rounds to 2 decimals.
