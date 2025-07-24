######### 1.2 ######
import pgzrun # imports the pgzrun module

#Define the height $ width of the game window, & the size of 

GRID_WIDTH = 16
GRID_HEIGHT = 12
GRID_SIZE = 50

WIDTH = GRID_WIDTH * GRID_SIZE
HEIGHT = GRID_HEIGHT * GRID_SIZE

MAP = ["WWWWWWWWWWWWWWWW",
       "W              W",
       "W              W",
       "W  W   KG      W",
       "W  WWWWWWWWWW  W",
       "W              W",
       "W       P      W",
       "W  WWWWWWWWWW  W",
       "W       GK     W",
       "W              W",
       "W              W",
       "WWWWWWWWWWWWWWWW"]
# Convert grid (x, y) to screen pixel coordinates
def GetScreenCoords(x, y):
    return (x * GRID_SIZE, y * GRID_SIZE)
# Draw floor tiles
def DrawBackground():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            pgzrun.screen.blit("floor1", GetScreenCoords(x, y))
# Setup player
def GetActorGridPos(actor):
    return(round(actor.x / GRID_SIZE), round(actor.y / GRID_SIZE))
def SetupGame():
    global player
    player = pgzrun.Actor("player", anchor=("left", "top"))
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            square = MAP[y][x]  # pad in case row is short
            if square == "P":
                player.pos = GetScreenCoords(x, y)
# Draw walls and doors
def DrawScenery():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            row = MAP[y].ljust(GRID_WIDTH)
            square = row[x]
            pos = GetScreenCoords(x, y)
            if square == "W":
                screen.blit("wall", pos)
            elif square == "D":
                screen.blit("door", pos)
            # You can add more tile types like "K", "G" here later
# Main draw loop
def drawActors():
    player.draw()
def draw():
    screen.clear()
    DrawBackground()
    DrawScenery()
    drawActors()
######
def MovePlayer(dx, dy):
    (x, y) = GetActorGridPos(player)
    x += dx
    y += dy
    square = MAP [y][x]
    if square == "W":
        return
    elif square == "D":
        return
    player.pos = GetScreenCoords(x,y)
# Setup and run
SetupGame()
pgzrun.go()

pgzrun.go()

def GetScreenCoords(x,y):
    return(x* GRID_SIZE, y * GRID_SIZE)


def DrawBackGround():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            screen.blit("floor", GetScreenCoords(x,y))


