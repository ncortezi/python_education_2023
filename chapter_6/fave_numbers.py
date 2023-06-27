favorite_numbers = {
	'nick':[1,2,3,4],
	'tucc':[23],
	'coco':[2,4,5,6],
	'pat':[1,4,5,7,6]
}

for name, nums in favorite_numbers.items():
	print(f"{name.title()}'s favorite numbers are:")
	for num in nums:
		print(f"\t{num}")