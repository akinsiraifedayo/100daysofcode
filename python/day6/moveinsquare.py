def turn_right():
    turn_left()
    turn_left()
    turn_left()

def move_in_square():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_right()
    move()

move_in_square()