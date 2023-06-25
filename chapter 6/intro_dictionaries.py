#dictionaries allow us to associate multiple key/value pairs to a single entity
#they are created using dict_name =  {} 
#within the {}, we create linked values using key:value - pairings

nick = {
	#key    #value
	'age' : 30, 
	'name' : 'Nick',
	} 

print(nick['age'])
			#call the key and 30 is returned as the value
print(nick['name'])

# we can also assign the values to a variable through the key

nick_age = nick['age']

# we can also add new key/value pairings to an existing dictionary

nick["hometown"] = "Baltimore"
nick["pet"] = "Taco & Belle"

print(nick)

#to change the value, we need to reassign by using the key

nick["age"] = 31
print(nick)

#we can also build new entries from a blank dictionary

coco = {}

coco["age"] = 34
coco["hometown"] = "Monroe"

print(coco)