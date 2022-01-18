WIDTH = 1200
HEIGHT = 600

alien = Actor('alien')
alien.pos = 50, 50

def draw():
    screen.fill((51,255,255))
    alien.draw()

def update():
    alien.left += 3
    alien.top += 2
    if alien.top > HEIGHT:
        alien.pos = 50,50
