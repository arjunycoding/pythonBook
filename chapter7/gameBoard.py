def horizontalLine():
    return "___"
def verticalLine():
    return "|"
boardSize = int(input("What is the size of the board?"))
for i in range(boardSize):
    square = verticalLine() + horizontalLine()
    print(horizontalLine() * boardSize)
    print(verticalLine() * boardSize)
    # print(square * boardSize)
    # print(horizontalLine() * boardSize)