available_toppings = ["cheese","pepperoni","onions","mushrooms"]

requested_toppings = ["cheese","pepperoni","anchovies","pineapple"]

for topping in requested_toppings:
	if topping in available_toppings:
		print(f"Adding {topping} to your pizza")
	else:
		print(f"I'm sorry, we do not have {topping}")

print("Here's your pizza!")