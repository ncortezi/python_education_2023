pizzas = ["Pepperoni","Vodka","Grandma","Extra Cheese"]
friend_pizzas = pizzas[:]

pizzas.append("Veggie")
friend_pizzas.append("Hawaiian")

print("My favorite pizzas are:")
for pizza in pizzas:
	print(pizza)
	
print('\n')

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
	print(pizza)
	