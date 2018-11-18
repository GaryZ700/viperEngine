import viper
import time

#create new instances of the terminal graphics and input classes
TG = viper.TG([50,30], "center")
I = viper.I()
I.addKeyBinding("DOWN","a")


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

    if(I.lastKeyDown == "DOWN"):
        x+= 1
