glossary = {
	'list':"a collection of values stored on a liner array",
	'method':'an action called on a variable or value',
	'function':'an operation or action called upon arguments',
	'set':'a collection of unique items',
	'loop':'a function that triggers some action for every item in a collection'
}

print("Glossary: \n")
for k,v in glossary.items():
	print(f"{k}: {v}\n")