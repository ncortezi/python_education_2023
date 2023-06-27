#to exit a while loop immediately without running any remaining code regardless of conditional test we use a break statement

prompt = "\n Please tell me where you are from: "
prompt += "\n(Enter quit when you are finished)\n"

while True:
	city = input(prompt)

	if city ==  "quit":
		break
	else:
		print(f"I've never been to {city.title()}!")