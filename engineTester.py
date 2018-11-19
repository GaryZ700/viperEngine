import viper
import time

#create new instances of the terminal graphics and input classes
TG = viper.TG()

#set up input system
I = viper.I()

def moveUp():
    ship.y -= 2
def moveDown():
    ship.y += 2 
def moveLeft():
    ship.x -= 1
def moveRight():
    ship.x += 1

I.addKeyBinding("DOWN","whileKeyDown", [moveUp])
I.addKeyBinding("UP", "whileKeyDown", [moveDown])
I.addKeyBinding("LEFT", "whileKeyDown", [moveLeft])
I.addKeyBinding("RIGHT", "whileKeyDown", [moveRight])


ship = viper.VO(TG.loadImage("plane"))

#intialize main graphics screen

while(True):

    time.sleep(0.01);
    TG.addImage(ship.object, ship.x, ship.y)
    TG.refresh();
    TG.clearScreen();
    I.update()
