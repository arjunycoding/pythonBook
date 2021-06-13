petOrder = [
    "Pete the Pug", # 1
    "Sally the Simamse Cat", # 2
    "Beau the boxer", # 3
    "Lulu the Labrador", # 4
    # Cory the Corgi :: 5
    # Mimi            :: 6
    "Lily the Lynx", # 7
    "Pauline the Parrot", # 0
    "Gina the Gerbil", # -
    "Tubby the Tabby Cat" # 8
]
del petOrder[6]
# del petOrder[5]
petOrder[0:0] = ["Pauline the Parrot"]
petOrder[5:5] = ["Cory the Corgi"]
petOrder[5:5] = ["Mimi the Maltese Cat"]
del petOrder[4]
del petOrder[7]
print(f"The order of the pet parade is: {petOrder}")