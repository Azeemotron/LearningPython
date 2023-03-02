# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

# A challenge on Reborg's World. Some functions already define on site.

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while at_goal() == False:  # Remember that it's '==' not '='. 'False' must also be capital 'F'
    jump()

# We could also use the while not at_goal():  As the 'not' keyword flips the condition

# A while loop can become an infinite loop if it's given a condition that will make it last forever

# It worked
