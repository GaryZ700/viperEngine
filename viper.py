#Gary Zeri
#2321569
#zeri@chapman.edu
#CPSC230-10
#For Fun

#wrapper to provide acess to all of Viper's Features without having to acess each feature separtely one by one

import sys

#add in paths to all of the viper engine features
sys.path.append(sys.path[0]+"/viper/terminalGraphics")
sys.path.append(sys.path[0]+"/viper/input")
sys.path.append(sys.path[0]+"/viper/viperObject")

#begin importing all important engine modules
from terminalGraphics import terminalGraphics as TG
from input import input as I
from viperObject import viperObject as VO
