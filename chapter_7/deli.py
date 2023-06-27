sandwich_orders = ["Pastrami","Reuben", "Italian","Turkey & Swiss","Pastrami","Pastrami","Ham & Cheese","Reuben","Muffaletta"]
finished_sandwiches = []

print("We are sorry, but we are out of Pastrami!\n")

while "Pastrami" in sandwich_orders:
	sandwich_orders.remove("Pastrami")

while sandwich_orders:
	current_sandwich = sandwich_orders.pop()
	print(f"Your {current_sandwich} has been made!")
	finished_sandwiches.append(current_sandwich)

print('\n')

finished_sandwiches.reverse()

for sandwich in finished_sandwiches:
	print(f"I have made a {sandwich}")