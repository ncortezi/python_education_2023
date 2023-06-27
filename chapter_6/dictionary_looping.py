user_0 = {
	'username':'efermi',
	'first':'enrico',
	'last':'fermi',
}

#we can use .items() method when looping through a dictionary to return key/value pairs 
# you have to put both the key & the value markers in the opening for loop before the in

for key, value in user_0.items():
	print(f"\n{key}: {value}")

#if we just want to return keys, we can use the .keys() method

for key in user_0.keys():
	print(key)

#if we want just values, we can use the .values() method

for value in user_0.values():
	print(value.title())

#if we want to return only unique values, we can use the set() function

