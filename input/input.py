#Gary Zeri
#2321569
#zeri@chapman.edu
#CPSC230-10
#For Fun

#input object allows developers to easily gain access to real time input with python
class input():

    import msvcrt

    #init global variables

    #init empty dictonary for holding keyBinders
    #holds subslist containg key to listen for, and code to execute given certain certain condition
    #ex, onKeyUp, onKeyDown, whileKeyDown, or False, if no action to be taken
    keyBinders= {}

    #holds string of lastKeyUp/Down
    lastKeyUp = ""
    lastKeyDown = ""

    #holds string of current key being held
    currentKeyDown = ""

###############################################################################

    #initialization function for the input class
    #returns instance of the input class
    #self, refers to instance of this class
    #keyBinders, refers to intial list of keys to listen to, default is none
    def __init__(self, keyBinders={}):

        #assign keyListeners to instance of this class
        self.keyBinders = keyBinders

###############################################################################

    #addKeyBinding function
    #has no return value
    def addKeyBinding():
        pass

###############################################################################

    #modifyKeyBinding function
    #has no return value
    def modifyKeyBinding():
        pass

###############################################################################

    #updateInput function
    #returns any keys that were just pressed on the keyboard, returns False if no keys were pressed
    def updateInput():
        pass

###############################################################################
