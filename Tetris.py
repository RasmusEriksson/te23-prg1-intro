
from time import sleep


gameBoard = dict()

squaresX = 10
squaresY = 20

tickSpeed = 1

for i in range(squaresX):
    column = i+1
    gameBoard[str(column)] = dict()

    for i2 in range(squaresY):
        row = i2+1
        gameBoard[str(column)][str(row)] = " "


def changePosition(oldPosition,newPosition):
    print("hi")


def renderList():
    for i in range(squaresY):
        row = i+1

        rowRenderList = []

        for i2 in range(squaresX):
            column = i2+1
            rowRenderList.append(gameBoard[str(column)][str(row)])

        print("︱".join(rowRenderList))

game = True

squarePos = dict()
squarePos["x"] = 5
squarePos["y"] = 0

newPos = squarePos

while game == True:



    squarePos = newPos
    newPos = squarePos
    newPos["y"] += 1

    changePosition(squarePos,newPos)
    
    
    renderList()

    

    sleep(tickSpeed)
