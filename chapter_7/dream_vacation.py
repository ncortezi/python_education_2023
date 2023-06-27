vacations = {}

polling_active = True

while polling_active:
	name = input("What is your name?\n")
	place = input("Where would you like to visit?\n")

	vacations[name] = place 

	repeat = input("Is there someone else here to answer? (yes/no)\n")

	if repeat == "no":
		polling_active = False

print("\n----POLL RESULTS----")
for k,v in vacations.items():
	print(f"{k.title()} would love to go to {v.title()}!")