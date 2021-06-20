print("Input a word")
word = input()
numOfA = 0
numOfE = 0
numOfI = 0
numOfO = 0
numOfU = 0

for i in word:
    if(i.lower() == "a"):
        numOfA += 1
    elif(i.lower() == "e"):
        numOfE += 1
    elif(i.lower() == "i"):
        numOfI += 1
    elif(i.lower() == "o"):
        numOfO += 1
    elif(i.lower() == "u"):
        numOfU += 1
letterReport = f"""
    Number Of A's in {word}: {numOfA}
    Number Of E's in {word}: {numOfE}
    Number Of I's in {word}: {numOfI}
    Number Of O's in {word}: {numOfO}
    Number Of U's in {word}: {numOfU}
"""

print(letterReport)