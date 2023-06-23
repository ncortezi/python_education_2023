#five places I'd like to visit in unordered list

places = ["Tokyo", "Berlin", "Sydney", "Shanghai","Austin"]

#temporarily sort list
print(sorted(places))
print('\n')
print(places)
print('\n')
#temporarily sort list in reverse

print(f"{sorted(places,reverse=True)} \n")

#reverse list

places.reverse()
print(f"{places}\n")

#reverse list to original

places.reverse()
print(f"{places}\n")

#sort list alphabetically

places.sort()
print(f"{places}\n")

#reverse search

places.sort(reverse=True)
print(f"{places}\n")