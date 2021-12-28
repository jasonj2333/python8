#biblioteka
def go(steps=1):
    for i in range(steps):
        move()

def turn_right():
    repeat 3:
        turn_left()

def take_object():
    while object_here():
            take()

def put_object():
    while carries_object():
            put()

