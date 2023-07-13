
def list_order(*toppings):
	print("Thank you for your order! Your pizza will include: ")
	for topping in toppings:
		print(f"- {topping}")

def get_order():
	active = True
	order = ["cheese"]
	new_topping = ""
	greeting = "Welcome to Pizza Palace!\n"
	order_screen = input("What you like to add to your pizza? Enter 'No' to quit\n")
	if order_screen == "No":
		active = False
		list_order(order)
	while active:
		new_topping = order_screen
		order.append(new_topping)

get_order()