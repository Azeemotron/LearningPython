# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

# A challenge on Reborg's World. Some functions already define on site.

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while wall_on_right() == True:
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear() == True:
        move()
    turn_left()

while not at_goal():
    if front_is_clear() == True:
        move()
    elif wall_in_front() == True:
        jump()

# It worked
