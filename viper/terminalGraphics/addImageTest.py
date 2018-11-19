from terminalGraphics import terminalGraphics
TG = terminalGraphics()

image = TG.loadImage("plane")

TG.addImage(image, 10, 20)

TG.refresh()
