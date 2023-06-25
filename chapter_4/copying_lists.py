#we can use slicing to easily copy parts or the whole of list to a new list

#if we want to copy a full list, we slice with '[:]' with no index points on either side of bracket

numbers_one = [1,2,3,4,5,6]
numbers_two = numbers_one[:]
print(f"{numbers_two}\n")

#we can prove that the lists are unique by adding an additional number 

numbers_two.append(7)
print(f"Here is list one: {numbers_one}")
print(f"Here is list two: {numbers_two}\n")

#you CANNOT just assign a preexisitng list as a variable like below

animals = ["Dog","Cat","Monkey"]
other_animals = animals

#this just has the variable point back to the original list, not create a new list

