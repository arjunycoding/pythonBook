zeroLegs = 0
twoLegs = 0
fourLegs = 0

moose = 4
snake = 0
penguin = 2
lion = 4
monkey = 2
dolphin = 0
bear = 2
elephant = 4
giraffe = 4
koala = 2
shark = 0
kangaroo = 2
komodoDragon = 4

numberOfLegs = [4, 0, 2, 4, 2, 0, 2, 4, 4, 2, 0, 2, 4]

for i in range(len(numberOfLegs)):
    print(numberOfLegs[i])
    if numberOfLegs[i] == 0:
        zeroLegs += 1
        #print("0")
    elif numberOfLegs[i] == 2:
        twoLegs += 1
        #print("2")
    elif numberOfLegs[i] == 4:
        fourLegs += 1
        #print("4")

summary = f"""
    Animals with no legs: {zeroLegs}
    Animals two legs: {twoLegs}
    Animals four legs: {fourLegs}
"""
print(summary)