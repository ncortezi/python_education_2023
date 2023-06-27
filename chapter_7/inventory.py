inventory = {
	"head":"helmet",
	"chest":"tunic",
	"legs":"boots",
	"ring":"fire-walker",
}

message = input("What would you like to check? ").lower()

if message in inventory.keys():
	print(f"You are currently wearing a {inventory[message].title()} in the {message.title()} slot")
else:
	print(f"You do not have anything equipped in that slot")

switch = input("Would you like to change this item? ").lower()

if switch == "yes":
	new_item = input("What would you like to equip? ").lower()
	inventory[message] = new_item
	print(f"You have equipped {inventory[message].title()} in the {message.title()} slot")
else:
	print("Good luck on your adventure!")