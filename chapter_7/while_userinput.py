#we can use while loops to continue to request user input until a certain condition is met

prompt = "\n I am a parrot!"
prompt += "\n if you want me to shut-up, tell me to quit! "

message = ""

while message != "quit":
	message = input(prompt)
	if message != "quit":
		print(message)

