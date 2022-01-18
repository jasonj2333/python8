def redefine(fn):
    def wrapper():
        fn()
        recording_state = recording(False)
        x, y = position_in_front()
        if ( RUR.is_pushable("box", x, y) and RUR.is_obstacle("water", x, y) and not RUR.is_bridge("bridge", x, y)):
            RUR.remove_obstacle("water", x, y)
            RUR.remove_pushable("box", x, y)
            RUR.add_decorative_object("water", x, y)
            RUR.add_object("bridge", x, y)
        recording(True)
        RUR.record_frame()
    return wrapper

move = redefine(move)

RUR.add_pushable("box", 2, 1)
RUR.add_obstacle("water", 3, 1)
move()
move()
move()