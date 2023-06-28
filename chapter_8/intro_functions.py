#functions are blocks of code designed to do one specific job
#python comes with a number of pre-written funcitons, but we can write our own

def greet_user():
	print("Hello!\n")

greet_user()


#we can also include arguments that will be passed into the codeblock below
def greet_name(username):
	print(f"Hello {username.title()}!\n")

greet_name("Nick")

#we can include multiple arguments, but positioning of instances matters!

def hello_pet(name,pet_name):
	print(f"Hello {name.title()}! I see you brought your pet {pet_name}!\n")

hello_pet("Nick","Taco")

#but we can use keyword arguments to switch the positions of the instances

hello_pet(pet_name="Belle",name="Coco")

#we can also set a default value to insert if nothing is included in the argmts

def pizza(name, toppings = "plain"):
	print(f"{name.title()} would like a {toppings.lower()} pizza!\n")

pizza("Nick","Pepperoni")

pizza("Coco")

#when using default values, any parameter with a default value needs to be lsited after all that don't

#we can make an argument optional by setting the default value to an empty "" but be sure to include if conditions!

def print_name(first,last,middle =''):
	if middle: #remember, this means IF there is a value for middle
		print(f"{first} {middle} {last}\n")
	else:
		print(f"{first} {last}")

print_name("Nick","Cortezi","Dominic")
print_name("Chris","Cortezi")