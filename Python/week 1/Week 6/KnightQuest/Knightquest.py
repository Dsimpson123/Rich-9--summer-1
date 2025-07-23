######### 1.2 ######
import pgzrun # imports the pgzrun module

#Define the height $ width of the game window, & the size of 

GRID_WIDTH = 16
GRID_HEIGHT = 12
GRID_SIZE = 50

WIDTH = GRID_WIDTH * GRID_SIZE
HEIGHT = GRID_HEIGHT * GRID_SIZE

pgzrun.go()

def GetScreenCoords(x,y):
    return(x* GRID_SIZE, y * GRID_SIZE)


def DrawBackGround():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            screen.blit("floor", GetScreenCoords(x,y))
