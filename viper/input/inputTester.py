import msvcrt
import time
from input import input
i = input()
i.addKeyBinding("UP", "a")

while(True):

    time.sleep(0.1)
    i.update()
    print(i.currentKeyDown + "THIS KEY IS CURRENTLY Down")
