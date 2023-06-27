prompt = "\nWelcome to the theater! How old are you?\n"
prompt += "When you have added your party, please enter quit\n"

total = 0

while True:
	age = input(prompt)

	if age == 'quit':
		break

	age = int(age)

	if age < 3:
		print("Kids get in free")
	elif age < 12:
		print("That will be $10!")
		total += 10
	else:
		print("That will be $15!")
		total += 15

print(f"\nYour total is ${str(total)}! Enjoy the movie!")