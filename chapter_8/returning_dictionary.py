#we can use functions to build or modify more complex data types like lists & dicts

def build_person(first_name,last_name):
	person = {'first':first_name,'last':last_name}
	return person 

musician = build_person("matt","bellamy") #musician here is the dictionary, not a variable or single data type

print(musician)


#we can add default or optional arguments as well

def pet_finder(name,breed,age=''):
	pet = {'name':name,'breed':breed}
	if age:
		pet['age'] = age
	return pet

taco = pet_finder("Taco","Cat",4)
belle = pet_finder("Belle","Cat")

print(taco)
print(belle)