#Using append, pop, remove, & insert

cities = ["Baltimore","Austin", "Tokyo","Philadelphia","Boston","London"]

#use append to add new city.

cities.append("Frankfurt")
cities.append("Shanghai")
cities.append("Monroe")
cities.append("New York")

#use .pop() to remove last city

last_city = cities.pop()

print(cities)
print(last_city)
print("\n")

#use .pop() to remove third city
third_city = cities.pop(2)
print(cities)
print(third_city)
print('\n')

#use .remove() to remove city by value
cities.remove("Austin")
print(cities)
print('\n')

#use .remove to remove city with variable
remove_city = "Baltimore"
cities.remove(remove_city)
print(cities)
print('\n')

#use insert to add cities at beginning & middle of list
cities.insert(0,"Towson")
cities.insert(4,"Prague")
cities.insert(2,"San Diego")
print(cities)
print('\n')

#print temporarily sorted & temporarily reversed lists
print(sorted(cities))
print(sorted(cities,reverse=True))
print(cities)
print('\n')

#perm sort then reverse list
cities.sort()
print(cities)
cities.sort(reverse=True)
print(cities)
print('\n')

#find length of cities, delete using DEL
print(len(cities))
del cities[1]
print(len(cities))
print(cities)