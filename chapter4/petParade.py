petOrder = [
    "Pete the Pug",
    "Sally the Simamse Cat",
    "Beau the boxer",
    "Lulu the Labrador",
    "Lily the Lynx",
    "Pauline the Parrot",
    "Gina the Gerbil",
    "Tubby the Tabby Cat"
]
# "Pauline the Parrot",
# "Pete the Pug",
# "Sally the Simamse Cat",
# "Beau the boxer",
# "Lulu the Labrador",
# "Lily the Lynx",
# "Mimy the Maltese Cat"
# "Cory the Corgi"
# "Tubby the Tabby Cat"

del petOrder[6]
print(f"The order of the pet parade is: {petOrder}")
del petOrder[5]
petOrder[0:0] = ["Pauline the Parrot"]
print(f"The order of the pet parade is: {petOrder}")

petOrder[6:6] = ["Cory the Corgi"]
petOrder[6:6] = ["Mimy the Maltese Cat"]
print(f"The order of the pet parade is: {petOrder}")

del petOrder[4]
del petOrder[4]


















# del petOrder[6]
# petOrder[0:0] =  ["Pauline the Parrot"]
# print(f"The order of the pet parade is: {petOrder}")
# del petOrder[5]
# print(f"The order of the pet parade is: {petOrder}")
# petOrder[5:5] = ["Cory the Corgi"]
# petOrder[5:5] = ["Mimy the Maltese Cat"]
# print(f"The order of the pet parade is: {petOrder}")
# del petOrder[4]
# del petOrder[6]
# print(f"The order of the pet parade is: {petOrder}")