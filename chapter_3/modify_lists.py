#you can modify a value in a list be reassigning it through it's index position

names = ["Nick", "Coco", "Taco", "Belle"]

print(names)

names[0] = "Frank"
print(names)

#you can add new items to a list using the .append() method

names.append("Nick")
print(names)

names.append("Carl")
names.append("Cynthia")
print(names)

# you can delete items from a list using the del statement. Syntax is del list[x]

del names[0]
print(names)

