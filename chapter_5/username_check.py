current_users = ["Nick","Frank","Steve","Bob","Mike"]
current_users_lower = []

for user in current_users:
	current_users_lower.append(user.lower())

new_users = ["Frank","Bill","Steve","Dwight","Ann","mike"]

for user in new_users:
	if user.lower() in current_users_lower:
		print("Sorry, please select a new username")
	else:
		print(f"Welcome! Your user name is {user}")