#to permanently order a list, use to .sort() method. note this cannot be used IN a print command as it changes the actual list

names = ["Steve", "Bob", "Alexander", "Greg", "Nick", "Roger"]
print(names)

names.sort()

print(names)

#we can also reverse the order by passing the argument 'reverse=True'

numbs = [1,5,3,7,2,9,8,6]

numbs.sort(reverse=True)

print(numbs)

#to temporarily sort a list, we use the sorted() FUNCTION

animals = ["Cat", "Mouse", "Dog", "Zebra", "Hen", "Alligator"]

print(sorted(animals, reverse=True))
print(animals)

#to reverse the order of an original list (not sort it descending), we can use the .reverse() method

colors = ["Red", "Yellow", "Green", "Blue", "Purple", "White"]
colors.reverse()
print(colors)

#to get the length of a list, we can use the len(x) function

digits = [1,2,6,5,43,6,57,4,3,5,6]
length_dig = len(digits)
print(length_dig)