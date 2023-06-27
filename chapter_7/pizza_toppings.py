prompt = "\nWhat would you like on your pizza? \n"

active = True

while active:
	message = input(prompt)
	if message != "quit":
		print(f"Adding {message} to your pizza!")
	else:
		active = False

print("\nHope you enjoy your pizza!")