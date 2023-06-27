cities = {
	'baltimore': {
		'state':'maryland',
		'population':"ten million",
		'bird':'oriole',
	},
	'new york city': {
		'state':'new york',
		'population':"thirty four million",
		'bird':'cardinal'
	},
	'philadelphia': {
		'state':'pennsylvania',
		'population':"eight million",
		'bird':'eagle'
	},
}

for city,info in cities.items():
	print(f"Here's some fun facts about {city.title()}\n") #pulls the first key *cities*
	for inf,fo in info.items(): #.items() lets the for loop know to be looking for a k/v pair for eachs
		print(f"The {inf} of {city.title()} is {fo.title()}")
	print('\n')
