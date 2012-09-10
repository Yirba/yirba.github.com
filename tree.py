############################################
# tree.py                                  #
# Developed by Yirba <http://yirba.x10.mx> #
# Created: 10 September 2012               #
# Last modified: 10 September 2012         #
############################################
# Description:                             #
#   Prints a tree out of asterisks in the  #
# specified size. For best results,        #
# treeWidth should be an odd multiple of   #
# 3.                                       #
############################################

def printCrown(treeWidth):
    for i in range(1,treeWidth+1,2):
        print(("*"*i).center(treeWidth))

def printTrunk(treeWidth, trunkHeight):
    for i in range(trunkHeight):
        print(("*"*int(treeWidth/3)).center(treeWidth))

def printTree(treeWidth, trunkHeight):
    printCrown(treeWidth)
    printTrunk(treeWidth, trunkHeight)

printTree(9,3)
