#Gary Zeri
#2321569
#zeri@chapman.edu
#CPSC230-10
#For Fun

#Game Engine provides several methods and tools to help create games via python for the terminal
#uses terminalGraphics to provide text based graphics abillities
#uses termianlAnimation to provide terminal level animation of text
class viper():

    #import needed modules
    import time
    import sys

    #begin by initializign python path for the viperEngine setup
    sys.path.append(sys.path[0]+"/terminalGraphics")

    from terminalGraphics import terminalGraphics

#    from terminalAnimation import terminalAnimation

    #prepare terminalGraphics and terminalAnimation class instance variables
    #TG = False
    #TA = False

    #import needed assets from gameEngineAssets class
    #from gameEngineAssets import scene

    #init global variables here
    #dictionary to hold all game scenes
    scenes = {}

    #variable that holds the current game scene
    currentScene = False

    #init frameRate variable
    FPS = 1

###############################################################################

    #initialization function for the gameEngine class
    #has no return value
    #height, int height of game to be maintained at all times
    #length, int length of game to be maintained at all times
    #screenPosition, relative position on the overall terminal screen, current only value possible is 'center'
    #FPS, how many frames per second should there be? Can be a float
    #layers, number of layers to use for the terminalAnimation class
    def __init__(self, height=50, length=70, screenPosition="center", FPS=1.0, layers=1):

        #init terminalGraphics class
        self.TG = self.terminalGraphics([length, height], screenPosition)

        #init termianlAnimation class
    #    self.TA = self.terminalAnimation(self.TG, layers=layers)

        #set FPS rate
        self.FPS = FPS

###############################################################################

    #createScene function
    #has no return value
    #self, instance of terminalGameEngine class
    #sceneName, string of name for scene
    #bgMap is terminalGraphics screen list with an object drawn into it
    #sprites refers to dictionary of sprites to add to the scene
    def createScene(self, sceneName, bgMap, sprites={}):

        #add new scene to scenes dictionary
        self.scenes[sceneName] = self.scene(bgMap, sprites)

###############################################################################

    #loadScene function
    #has no return value
    #self is reference to instace of the current class
    #sceneName refers to string of scene name
    def loadScene(self, sceneName):

        #check if scene name exists within the scence dictionary
        #if not print an error message
        if ( not (sceneName in self.scenes)):
            print("\n Scene '", sceneName, "does not exist! \n Did you mean to use createScene('", sceneName, "') instead?")

        else:
            # if yes update the game engine's current scene with the specifed scene
            self.currentScene = self.scenes[sceneName]

            #force update of screen to new scene
            self.updateScreen(redraw=True)

###############################################################################

    #wait function
    #self refers to instance of the terminalGameEngine class
    #seconds, refers to how long should the game wait in seconds
    def wait(self, seconds):
        self.time.sleep(seconds)

###############################################################################

    #updateSCreen function
    #self, refers to instance of the terminalGameEngine class
    #should entire screen be redrawn from scratch or should screen up updated , True or False
    def updateScreen(self, redraw=False):

        #if entire screen is to be redrawn, then update the image's background as well
        if(redraw):
            self.TA.animationScreen[0] = self.currentScene.bgMap

        #update all sprites in the scene
        #iterate through all sprites in the current scene
        for sprite in self.currentScene.sprites:

            #get actual sprite object from key to sprites dictionary
            sprite = self.currentScene.sprites[sprite]

            #if sprite has moved, update sprite position on the animation screen
            #or if screen is being redrawn from scratch, then redraw all sprites
            if(sprite.core.redraw or redraw):

                #update terminalAnimation screen by passing in sprite
                self.TA.update(sprite.core)

            #flatten animationScreen
            self.TA.flatten()

###############################################################################

    #update Input function
    #gets

###############################################################################

    #update function
    #self, refers to instance of the terlminalGraphics class
    #has no return value
    def update(self):

        #wait half a second before refreshing screen
        self.wait(self.FPS)

        #check for input from the user
        self.updateInput()

        #update the game screen
        #self.updateScreen()
