message = input("Hello! How many will be joining us today? ")

message = int(message)

if message > 8:
	print("I'm sorry, but there is a wait")
else:
	print("Right this way!")