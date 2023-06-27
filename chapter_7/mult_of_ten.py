message = input("Please enter a number: ")
message = int(message)

if message % 10 == 0:
	print("That is a multiple of ten")
else:
	print("That is not a multiple of ten")