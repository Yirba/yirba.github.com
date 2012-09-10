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
