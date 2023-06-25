#we can use values to effect other values in the dictionary

alien = {
	"space": 1, 
	"speed": "high",
	"name":"Gorzo",
	}
print(f"Alien is at {alien['space']} on the board")

if alien["speed"] == "low":
	move = 1
elif alien["speed"] == "medium":
	move = 2
else:
	move = 3

alien["space"] = alien["space"] + move

print(f"Alien is now on {alien['space']} on the board\n")


#we can also delete key/value pairings by using the del function

print(alien)
del(alien['name'])
print(alien)

print('\n')

#finally, we can use the .get() method to throw a message if a specific key does not exist in the dictionary

print(alien.get("homeplanet","He has no home"))