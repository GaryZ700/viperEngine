#Gary Zeri
#2321569
#zeri@chapman.edu
#CPSC230-10
#For Fun

#viperObject class
#Object designed to allow for multiple viper engine parts to interact and to aid in
#object oriented programming styles
class viperObject():

    #global variables defined here

    #x, y coordinates of this object in relation to the overall terminalGraphics screen
    #x and y refer to bottom right most point of the object
    x = 0
    y = 0

    #object refers to main object, can be either list of objects,
    #or screen map representing an image
    #regardless of its contents must be a list
    object = []

    #componets refers to list of other viperEngine classes that can be added to extend the functionality of this class
    componets = []

    #functions, list of functions written by the user to extend the abillites of this class
    functions = []

###############################################################################

    #intialization function for the viperObject class
    #returns new instance of the viperObject class
    #self, reference to instance of the viperObject class
    #objectArg, main child of this object, please see above for more information, default is an empty list
    #xArg, refers to intial x position of this object
    #yArg, refers to intial y position of this object
    #componetsArg, list of viperEngine componets to extend the abillities of this object
    #functionsArg, list of functions to call each update on this object that the user wrote to extend this class
    def __init__(self, objectArg=[], xArg=0, yArg=0, componetsArg=[], functionsArg=[]):

        #intialize class variables with passed in args
        self.object = objectArg
        self.x = xArg
        self.y = yArg
        self.componets = componetsArg
        self.functions = functionsArg

###############################################################################

    #update function
    #has no return value
    #self refers to instance to of the viperObject class
    def update(self):

        #iterate through all viperComponets
        for componet in componets:
            componet.update()

        #iterate through all functions passed into this class , and execute each function
        for function in functions:
            function()
