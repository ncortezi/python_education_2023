#we can use lists in functions to quickly parse through or modify a list 

messages = ["Hello!","Goodbye!","Try Again?","Game Over!"]

def show_messages(messages):
	for message in messages:
		print(f"{message}")
show_messages(messages)


'''
'''
#SEND MESSAGES

#if we want to prevent a function from modifying or changing the original list, we can put a [:] after the variable name in the function call
#this will create a copy of the list that will be acted on

unsent_messages = ["Checking in!","Good Morning!","Good Night!"]
sent_messages = []
def send_messages(messages,new_messages):
	messages.reverse()
	while messages:
		send_message = messages.pop()
		print(f"Sending New Message: {send_message}")
		new_messages.append(send_message)

send_messages(unsent_messages[:],sent_messages) #[:] creates a copy of the unsent_messages list, rather affecting the original list

print(unsent_messages) 
print(sent_messages)
#



