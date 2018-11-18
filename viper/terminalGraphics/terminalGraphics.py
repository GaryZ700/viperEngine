#Gary Zeri
#2321569
#zeri@chapman.edu
#CPSC230-10
#For Fun

import sys
import shutil

#graphic Terminal class
#provides a set of tools to python developers to work with creating terminal artwork
class terminalGraphics():

    #global variables defined here

    #init empty screen matrix
    screen = []

    #x is total length of terminal, and y is total height of terminal in text lines
    length = 0
    height = 0

    #where should screen be positioned relative to the overall terminal?
    #current value is only "center", or "full"
    #center draws screen in geographic x,y center of the terminal
    #bott-left, means that the bottom left of the screen should be drawn onto the bottom left of the terminal
    screenPosition=""

###############################################################################

    #initialization function for the terminal graphics class
    #returns new instance of the terminalGraphics class
    #self, reference to instance of the terminal graphics class
    #forcedSize, is [length,height] size of virtual screen that should be forced to be maintained, despite larger terminal screen
    #screenPosition, string representing where virtual screen should be drawn onto the screen, please see above line where variable is defined for further information on keywords usable
    def __init__(self, forcedSize=False, screenPosition="bott-left"):

        #check if screen size is to be forced to certain dimensions
        #if not, then use full terminal size as screen size
        if(forcedSize == False):
            #get dimensions of terminal screen
            dimensions = shutil.get_terminal_size()

            #set to total dimensions of terminal to global x and y variables
            #subtract one to account for lists begining to count from 0
            self.height = dimensions.lines - 1
            self.length = dimensions.columns -1

        #if forced size was specifed, then set screen height and width to specifed sizes
        else:
            self.height = forcedSize[1]
            self.length = forcedSize[0]

        #set screenPosition to specifed value, or default value
        self.screenPosition = screenPosition

        #update virtual screen object
        self.clearScreen()

###############################################################################

    #newScreen function
    #returns a new empty screen based upon the current screen size
    #self, refers to current instance of the terminalGraphics class
    def newScreen(self):

        #create empty new screen
        screen = []

        ##initialize empty text matrix with one index for each vertical text line in the terminal
        #and within that index initialize an empty string for each text column on the terminal
        #final result is a virtual "screen matrix" where each text "pixel"  can be accessed via screen[yPosition][xPosition]
        for y in range(self.height):
            screen.append([])
            for x in range(self.length):
                screen[y].append(" ")

        #return empty screen
        return screen

###############################################################################

    #clearScreen function
    #has no return value
    #self, reference to terminalGraphics class instance
    def clearScreen(self):

        #set screen to an empty screen matrix
        self.screen = self.newScreen()

###############################################################################

    #refresh fucntion
    #has no return value
    #self, instance of the terminalGraphics class
    def refresh(self):

        #get dimensions of terminal
        dimensions = shutil.get_terminal_size()

        #check where screen should be positioned
        #if screen should be placed at the center of the terminal,
        #then get appropriate padding for the top, bottom, and the sides of the screen
        if(self.screenPosition == "center"):

            #calculate how many lines should be above and below the game screen in order to center the screen
            verticalPadding =  (dimensions.lines - self.height - 1) // 2
            upperPadding = verticalPadding
            lowerPadding = verticalPadding

            #calculate how many spaces should be to the left and right of the screen
            horizontalPadding = (dimensions.columns - self.length - 1) // 2

            #get spacing before and after screen line to print
            spacingL = " " * horizontalPadding
            spacingR = spacingL + "\n"

        #if the bottom left of the screen is to be drawn onto the bottom left of the terminal then do so
        elif(self.screenPosition == "bott-left"):
            spacingL = ""
            spacingR = "\n"
            upperPadding = self.height - dimensions.lines
            lowerPadding = 0

        #print a carriage return to clear the terminal and print the screen to it
        sys.stdout.write("\r")

        #init empty string to hold total lines to print
        lineToPrint=""

        #print out top level padding for screen
        for paddingLine in range(upperPadding):
            lineToPrint += "\n"

        #for each line in the 2D representation of the terminal screen,
        #turn that line into a string and print it onto the terminal
        for line in self.screen:

            #add right spacing,
            lineToPrint += spacingL + "".join(line) + spacingR

        #print out bottom level padding for screen
        for paddingLine in range(lowerPadding):
            lineToPrint += "\n"

        #print all of line to print excluding final newline char
        #immdeialty flush out the screen to the terminal to ensure smooth framerate
        print(lineToPrint[:-1])
        sys.stdout.flush()

###############################################################################

    #drawPoint function
    #has no return value
    #self, reference to terminalGraphics class
    #point, [x,y] location of where to draw point
    #symbol, symbol to place at specifed point, default symbol is V
    def drawPoint(self, point, symbol="V"):

        #access (x,y) point on the screen and set symbol at that point
        self.screen[self.height - point[1] - 1][point[0]] = symbol

###############################################################################

    #drawVerticalLine function
    #self, reference to terminalGraphics class instance
    #x, integer refering to x value of vertical line
    #yPoint, [y0, y1], y values at which vertical line begins and ends
    def drawVerticalLine(self, x, yPoint, symbol="|"):

        #calculate dy
        dy = yPoint[0] - yPoint[1]

        #iterate through all y-values of vertical line
        for y in range(abs(dy) + 1):

            #change absolute y value to y value relative to the user's terminal screen
            y += yPoint[0]

            #draw a point at the specifed x and y value,
            #use specifed x value, and calculated y value
            self.drawPoint([ x, y ], symbol)

###############################################################################

    #drawline Functionn
    #has no return value
    #self, reference to instance of hte terminalGraphics class
    #point1, [x,y] point for starting point of a stright line
    #point2, [x,y] point for ending point of a stright line
    #symbol, string of symbol that is used to draw a straight line
    def drawLine(self, point1, point2, symbol="/"):

        #calculate delta x
        dx = point1[0] - point2[0]

        #calculate delta y
        dy = point1[1] - point2[1]


        #check if dx is zero to avoid division by zero and to draw a vertical line
        if(dx == 0):
            #draw a vertical line
            self.verticalLine(point1[1],point2[1])

        #calculate the slope of the line
        m = dy / dx

        #calcuate b for y = mx + b
        b = point1[1] - int(m*point1[0])

        #loop through all x values needed to draw the line
        for x in range(abs(dx)):

            #change x from absolute coordinate system to one relative to the user's terminal screen
            x += point1[0]

            #draw a point at the specifed x and y value,
            #use y = mx + b to calculate the y value
            self.drawPoint([ x, int(m*x) + b ], symbol)

###############################################################################

    #drawRect function
    #has no return value
    #self, reference to instance of terminalGraphics class
    #length, int of horizontal width of box
    #height, int of vertical height of box
    #origin, [x,y] where left-bottom point of box is drawn
    #verticalSymbol, text character to use to draw vertical sides of the rectangle
    #horizontalSymbol, text character to use to draw horizontal sides of the rectangle
    def drawRect(self, length, height, origin=[0,0], fill=" ", verticalSymbol="|", horizontalSymbol="-"):

        #REBUILD THIS METHOD
        #iterate through all y and x positions

        #iterate through all the dimensions needed to draw a box, (2)
            for dimension in range(2):

                yPosition = origin[1] + (dimension * height)
                xPosition = origin[0] + (dimension * length)

                #draw side lines with distance of "length" in between the two vertical lines
                self.drawVerticalLine( xPosition, [origin[1], origin[1] + height], verticalSymbol )

            for dimension in range(2):

                yPosition = origin[1] + (dimension * height)
                xPosition = origin[0] + (dimension * length)

                #draw top and bottom of boxes with distance of "height" in between the horizontal lines
                self.drawLine( [origin[0], yPosition], [origin[0] + length + 1, yPosition], horizontalSymbol )

###############################################################################

    #self is reference to instance of the terminalGraphics class
    #text is string of text to print
    #point refers to [x,y] cordinate of where first letter should be printed
    def drawText(self, text, point):

        #iterate through all chars within the text string
        for charNumber in range(len(text)):

            #calculate x and y position of current letter
            x = charNumber + point[0]
            y = point[1]

            #draw letter at correct point
            self.drawPoint([x,y], text[charNumber])
