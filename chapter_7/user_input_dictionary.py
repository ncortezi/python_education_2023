#we can use while loops to populate a dictionary with user input

responses = {}
polling_active = True

while polling_active: #remember, this condition is based on the flag variable above
	#prompt for name & response
	name = input("\nWhat is your name?\n") #this will be the key for each entry
	response = input("\nWhere would you like to visit one day?\n") #this will be the value

	responses[name] = response #adds a new k/v pair to the dictionary

	#then we ask if someone else will take the poll
	repeat = input("\nWould you like to let another person respond? (yes/no)\n")
	if repeat == "no":
		polling_active = False

print("\n---POLLING RESULTS---\n")
for k,v in responses.items():
	print(f"{k.title()} would like to visit {v.title()}")
print("\nThank you for taking the survey!")