#we use if / elif / else as conditional statements when parsing code

names = ["Nick","Greg","Coco","Jimmy"]

for name in names:
	if name == "Nick":
		print(name.upper())
	else:
		print(name.lower())

#like with for loops, we need to include a colon to announce an if statement & else statement

# we use == to determine equivalence

#we can use 'and' & 'or' to check multiple conditions

age_1 = 20
state = "CA"

if age_1 == 21 or state == "CA":
	print("You are allowed to drink here")
else:
	print("You are not allowed to drink here")