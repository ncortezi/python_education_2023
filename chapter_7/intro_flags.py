#we use flag variables as a signal to the program for systems where multiple conditions may end a while loop
#we set the flag to either True or False

active = True

prompt = "Tell Me Your Name and I Will Give It A Godly Title "

message = ""

while active:
	message = input(prompt)

	if message == "quit":
		active = False

	else: 
		message += " The God"
		print(message)
