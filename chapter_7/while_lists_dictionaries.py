#for modifying lists & dictionaries, we want to use WHILE loops not FOR loops

unadded_members = ["Steve", "Frank", "Bill", "Jim"]
added_members = []

while unadded_members: #remember, this means WHILE there are items in the lists
	add_member = unadded_members.pop()
	print(f"Adding {add_member.title()} to the list")
	added_members.append(add_member)

print('\n')

for member in added_members:
	print(f"{member.title()} has been added!")