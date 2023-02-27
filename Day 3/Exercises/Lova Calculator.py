# Day 3 - Exercise 4: Pizza Order Practice
# Exercise Completed & Checked via Coding Rooms Submission Checker

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lowerCaseNames = name1.lower() + name2.lower()

trueNameCount = lowerCaseNames.count("t") + lowerCaseNames.count("r") \
                + lowerCaseNames.count("u") + lowerCaseNames.count("e")

loveNameCount = lowerCaseNames.count("l") + lowerCaseNames.count("o") \
                + lowerCaseNames.count("v") + lowerCaseNames.count("e")

lovePercent = int(str(trueNameCount) + str(loveNameCount))  # Got to make them string first to place side by side

if lovePercent < 10 or lovePercent > 90:
    print(f"Your score is {lovePercent}, you go together like coke and mentos.")
elif 40 < lovePercent < 50:  # Once the 'ELIF' is true, it ignores all other statements and overrides them
    print(f"Your score is {lovePercent}, you are alright together.")
else:
    print(f"Your score is {lovePercent}.")