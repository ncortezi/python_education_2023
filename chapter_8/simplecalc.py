def add(x,y):
	return x + y 

def sub(x,y):
	return x-y
def mult(x,y):
	return x*y 
def div(x,y):
	return int(x/y)

prompt = input("Hello! What would you like to do? ")
total = 0
if prompt == "add":
	x = int(input("What is the first number?"))
	y = int(input("What is the second number?"))
	total = add(x,y)
elif prompt == "subtract":
	x = int(input("What is the first number?"))
	y = int(input("What is the second number?"))
	total = sub(x,y)
elif prompt == "multiply":
	x = int(input("What is the first number?"))
	y = int(input("What is the second number?"))
	total = mult(x,y)
elif prompt == "divide":
	x = int(input("What is the first number?"))
	y = int(input("What is the second number?"))
	total = div(x,y)
else:
	print("I'm sorry, that threw an error!")

print(f"\nThe answer is {total}")


