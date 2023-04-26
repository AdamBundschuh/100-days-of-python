# robot solution

def turn_three():
    turn_left()
    turn_left()
    turn_left()

right_counter = 0

while not at_goal():
    
    if right_counter > 3:
        move()
        right_counter = 0
    
    if right_is_clear():
        turn_three()
        move()
        right_counter += 1
    
    elif front_is_clear():
        move()
        right_counter = 0
    
    else:
        turn_left()
        right_counter = 0