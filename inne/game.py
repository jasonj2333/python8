WIDTH = 800
HEIGHT = 600

alien = Actor('alien')
alien.pos = 50, 0

def draw():
    screen.fill('green')
    alien.draw()

def update():
    alien.left += 2
    alien.top += 2
    if alien.top > HEIGHT:
        alien.pos = (50, 0)