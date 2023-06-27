favorite_places = {
	'nick':['tokyo','stone harbor'],
	'coco':['colorado','costa rica','new orleans'],
	'tucc':['baltimore']
}

for name, locations in favorite_places.items():
	print(f"{name.title()}'s favorite places are:")
	for location in locations:
		print(f"\t{location.title()}")
	print('\n')