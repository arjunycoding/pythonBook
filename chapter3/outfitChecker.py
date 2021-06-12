cherDress = "pink"
cherShoe = "white"
cherHasErrings = True
doinDress = "purple"
doinShoe = "pink"
doinHasErrings = True

print(f"At least one person is wearing purple{cherDress != doinDress}")
print(f"At least all pepole are wearing earings {cherHasErrings == True and doinHasErrings == True}")
print(f"At least one person is weraing pink {cherDress == 'pink' or doinDress == 'pink'}")
print(f"no one is weraing green {cherDress == 'green' and doinDress == 'green'}")
print(f"Every one's shoe color is the same {cherShoe != doinShoe}")
