message = input("What is your name? ")

user_names = ["nick","coco"]

print(f"Hello {message.title()}")

if message.lower() in user_names:
	print("Welcome back")
else:
	print("Are you sure you're in the right place?")