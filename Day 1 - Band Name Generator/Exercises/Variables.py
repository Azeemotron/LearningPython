# Day 1 - Band Name Generator: Exercise 4 - Variables
# Exercise Completed & Checked via Coding Rooms Submission Checker

# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

# My Logic here was as if there were 2 cups whose content you wanted to swap

c = a  # We have to introduce a 3rd cup to act as temporary storage
a = b  # 'a' Is now free to copy 'b' as it's contents won't be lost because 'c' has them
b = c  # 'b' Can now copy 'c' which is basically a replica of 'a'

#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)