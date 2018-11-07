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
    #{"key":["onKeyUp", functionReference]}
    keyBinders= {}

    #allKeys bool decides whether this function should listen to all keys on the keyboard
    allKeys = False

    #holds string of lastKeyUp/Down
    lastKeyUp = ""
    lastKeyDown = ""

    #holds string of current key being held
    currentKeyDown = ""

    #dictonary of keyboard arrows
    arrowKeys = {

    b'H':"UP",
    b'P':"DOWN",
    b'M':"RIGHT",
    b'K':"LEFT"

    }

###############################################################################

    #initialization function for the input class
    #returns instance of the input class
    #self, refers to instance of this class
    #keyBinders, refers to intial list of keys to listen to, default is none
    #allKeys, bool to decide if all keys should be listend to, default is False
    def __init__(self, keyBinders={}, allKeys=False):

        #assign keyListeners to instance of this class
        self.keyBinders = keyBinders

        #set allKeys bool
        self.allKeys = allKeys

###############################################################################

    #addKeyBinding function
    #has no return value
    #self, refers to instance of the input class
    #string of character to add binding to
    #event, string of keyboard event to listen to, all events are listed above
    #function, reference to function to execute upon event occurance, default value is False, no function used
    def addKeyBinding(self, key, event, function=False):

        #add in key to keyBinders
        self.keyBinders[key] = [event, function]

###############################################################################

    #modifyKeyBinding function
    #has no return value
    def modifyKeyBinding():
        pass

###############################################################################

    #update function
    #returns any keys that were just pressed on the keyboard, returns False if no keys were pressed
    #self, refers to instance of the input class
    def update(self):

        #check if there is input waiting to be acquired
        #if yes, then parse that input
        if(self.msvcrt.kbhit()):

            #get key from getch
            key = self.msvcrt.getch()

            #check if key is an arrow key
            if(key == b'\x00'):
                #if yes, get actual key value from msvcrt, and translate to arrow key from arrowKeys dictionary
                key = self.arrowKeys[self.msvcrt.getch()]

            #else if it is a regular key, then use decode to get regualar character
            else:
                key = self.msvcrt.getch().decode("ASCII")

            #check if key exist in the key bindings
            if(key in self.keyBinders or self.allKeys):

                #if yes, then update current current key press
                self.lastKeyDown = self.currentKeyDown
                self.currentKeyDown = key

        #if no keys are being pressed then update currentKey down as such and update lastKeyDown
        else:
            self.lastKeyDown = self.currentKeyDown
            self.currentKeyDown = ""

###############################################################################
