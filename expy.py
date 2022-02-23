# Write your code here :-)
from pygame import event
from pygame import quit
from pygame import font
from pygame import QUIT

def collidewall(player, wall, speed_x, speed_y):

    speed_x = abs(speed_x)
    speed_y = abs(speed_y)

    if player.colliderect(wall):
        if player[1] + player[3] <= wall[1] + speed_y:
            player.bottom = wall.top
        elif player[1] >= wall[1] + wall[3] - speed_y:
            player.top = wall.bottom
        elif player[0] + player[2] <= wall[0] + speed_x:
            player.right = wall.left
        elif player[0] >= wall[0] + wall[2] - speed_x:
            player.left = wall.right
        return True
    return False

def printText(surface, colour, text, x, y, size = 25):

    calibri = font.SysFont('calibri', size)

    text = str(text)
    label = calibri.render(text, False, colour)
    surface.blit(label,(x,y))

def check_exit():
    for e in event.get():
        if e.type == QUIT:
            quit()
            exit()
