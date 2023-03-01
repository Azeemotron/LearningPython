# Day 4 - Exercise 3: Treasure Map
# Exercise Completed & Checked via Coding Rooms Submission Checker

# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

# Write your code below this row 👇

x = int(position[0]) - 1  # We have to -1 because lists start counting at 0
y = int(position[1]) - 1

# This confused me at first, but essentially its stating that it is selected 'y' number list first
# It will then select 'x' number from THAT SELECTED list

map[y][x] = "X"

# So if xy is 23. It will select list 1 (2-1 from before) which is row2 (counting form 0)
# It will then select 1 (2-1) from row2 which is


# Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")