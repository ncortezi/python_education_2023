requested_toppings = ["Mushrooms","green peppers","pepperoni"]

for topping in requested_toppings:
	if topping.lower() == "mushrooms":
		print("We are out of that :(")
	else:
		print(f"Adding {topping.title()} to your pizza!")

print("Your pizza is done!\n")


#we can check if a list is empty prior and create conditions from there as well
#when the name of the list is used in an if statement, the system checks if it is empty returning False if empty and True if not

ice_cream_flavors = ["Cherry"]

if ice_cream_flavors:
	for flavor in ice_cream_flavors:
		print(f"Adding a scoop of {flavor}")
	print("Here's your ice cream!\n")
else:
	print("You just want vanilla?")
