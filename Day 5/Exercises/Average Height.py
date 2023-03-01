# Day 5 - Exercise 1: Average Height
# Exercise Completed & Checked via Coding Rooms Submission Checker

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

totalHeight = 0
numberOfStudents = 0
averageHeight = 0

for height in student_heights:
    totalHeight += height
    numberOfStudents += 1

averageHeight = totalHeight / numberOfStudents
print(round(averageHeight))
