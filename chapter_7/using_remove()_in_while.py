#we can use remove() in a while loop to remove all instances of a specific value from the list


animals = ["Dog","Cat","Dog","Monkey","Fish","Dog","Dog","Cat"]

while "Dog" in animals: #remember, this is WHILE there are instances of "Dog" in list animals
	animals.remove("Dog")

for animal in animals:
	print(f"Here is a {animal}")