import viper
import time

#create new instances of the terminal graphics and input classes
TG = viper.TG([50,30], "center")

#set up input system
I = viper.I()

I.addKeyBinding("DOWN","whileKeyDown")
I.addKeyBinding("UP", "whileKeyDown")
I.addKeyBinding("LEFT", "whileKeyDown")
I.addKeyBinding("RIGHT", "whileKeyDown")


#TG.loadImage()

#intialize main graphics screen

#init position for box
x = 0
y = 0

while(True):

    time.sleep(0.01);

    TG.refresh();
    TG.clearScreen();
    TG.drawRect(10,5,[x,y])

    I.update()
