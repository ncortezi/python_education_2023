#sometimes we want to use values and lists that CANNOT be changed or modified
#value that do not change are called IMMUTABLE
#lists that cannot change are called TUPLES

#tuples look just like a list, except we use ( ) instead of [ ] 

numbers = (1,2,3,4)

for i in numbers:
	print(i)

#if we try to reassign a value like numbers[0] = 4, an error gets throw 	

#tuples are technically defined by comma usage, so a one-element tuple MUST have a trailing comma

names = ("Nick",)

#while we can't write over a tuple, we can assign a new value to a variable representing the tuple

animals = ("Dogs", "Cats","Pigs")
print("original tuple of animals")
for animal in animals:
	print(animal)

print('\n')
animals = ("Birds","Monkeys","Fish")
print("Modified tuple of animals")
for animal in animals:
	print(animal)

#we are reassigning the VARIABLE, not modifying the previously associated tuple
