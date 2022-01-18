#--------------------- Lekcja Enter 3 ----
from library import *

think(100)

repeat 3:
    go()
    turn_right()
    go()
    turn_left()

go(6)
turn_right()
go(2)
turn_right()

repeat 4:
    go()
    turn_left()
    go()
    turn_right()

go(4)
put_object()
go()

# Pętla czujniki
from library import *

think(100)

while not at_goal():
    if front_is_clear():
        go()
    elif right_is_clear():
        turn_right()
    else:
        turn_left()