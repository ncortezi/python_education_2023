#python's range() function (not method) easily generates a range of numbers

for number in range(1,10):
	print(number)

#the range() function cuts off one before the y argument (1,10) = 1,2,3,4,5,6,7,8,9

#to convert a range() function directly into the list, we can use the list() function

numbers = list(range(15,20))

print(numbers)

for number in numbers:
	print(number)

#we can also use a third argument in range to skip over numbers when generating the range

even_numbers = list(range(2,11,2))
print(even_numbers)

#practice squaring numbers in list. Remember, we can do multiple actions in the for loop it self

squares = []

for value in range(1,11):
	sqr_value = value**2
	squares.append(sqr_value)

print(squares)