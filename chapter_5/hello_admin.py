usernames = ["Nick","Steve","Greg","Mike","admin"]


if usernames:
	for name in usernames:
		if name == "admin":
			print("Hello admin, would you like to see a status report?")
		else:
			print(f"Welcome back {name}!")
else:
	print("No users found")
