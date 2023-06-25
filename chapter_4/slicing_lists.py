# we use slicing to only select a particular part of a list. The syntax is similar to passing a y argument to an index pointer

#list[x:y] = x is starting position / y is ending position

numbers = [1,2,3,4,5,6,7,8,9]

print(numbers[0:4])

#the slice at the y is also one before the entered value 

#if we omit the beginning point, the slicer automatically pulls from the beginning

print("\n")

names = ["Nick","Chris","Greg","Frank"]

print(names[:2])

#if we omit the ending point, the slicer automatically pulls to the end

print("\n")

animals = ["Dog","Cat","Fish","Alligator"]

print(animals[2:])

#we can also use slices in loops to only loop within certain index parameters

print("\n")

players = ["Pele","Maradona","Messi","Ronaldo","Hart","Rooney"]

print("Here are the first three players on my team: \n")

for player in players[:3]:
	print(player)

print("\n")

print("Here are the last three players on my team:\n")

for player in players[3:]:
	print(player)