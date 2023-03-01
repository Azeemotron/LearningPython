# Day 5 - Exercise 3: Adding Even Numbers
# Exercise Completed & Checked via Coding Rooms Submission Checker


total = 0

for number in range(1, 101):  # The end of the range is not included, so if I want 100, I have to put 101
    if number % 2 == 0:  # Can work out even numbers by seeing if they have any remainder after / 2
        total += number

print(sum)

# Another method could have been:

# for number in range(2, 101, 2):
#   total += number
# print(sum)

# ^ This way, we start counting from 2, and we increment by 2 each time, guaranteeing only even numbers inc
