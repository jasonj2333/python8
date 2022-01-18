#biblioteka
def turn_right():
    repeat 3:
        turn_left()

def go(steps=1):
    for i in range(steps):
        move()
        take_object()

def take_object():
    objects = ["mlecz", "banan", "truskawka", "jabłko"]

    for object in objects:
        while object_here(object):
            take(object)

def put_object(object):
    while carries_object(object):
        put(object)

#Porządki w sadzie
from library import *

think(10)

turn_left()

repeat 11:
    while front_is_clear():
        go()
    if is_facing_north():
        turn_right()
        go()
        turn_right()
    else:
        turn_left()
        go()
        turn_left()

go(7)
objects = ["mlecz", "banan", "truskawka", "jabłko"]
for object in objects:
    put_object(object)
    go()