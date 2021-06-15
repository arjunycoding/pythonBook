friends = [
    "athtetic",
    "not athtetic",
    "older",
    "athtetic",
    "younger",
    "athtetic",
    "not athtetic",
    "older",
    "athtetic",
    "older",
    "athtetic"
]

bySwings = 0
byBasketballCourt = 0

for i in range(len(friends)):
    if friends[i] == "athtetic" or friends[i] == "younger":
        bySwings += 1
    else:
        byBasketballCourt += 1

print(f"Cats at Hula Hoops By Swings: {bySwings}\n Cats by Hula Hoops By Basketball Court: {byBasketballCourt}")