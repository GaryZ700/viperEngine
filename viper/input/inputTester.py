import msvcrt
import time
from input import input
i = input()

def test():
    print("DOwn")

def test2():
    print("Up")

i.addKeyBinding("UP", "whileKeyDown", [test])
i.addKeyBinding("UP", "whileKeyDown", [test2])


while(True):
    #print(msvcrt.kbhit())
    #if(msvcrt.kbhit()):
    #    msvcrt.getch()
    time.sleep(0.1)
    i.update()
