#we can use the min() max() and sum() functions to return the lowest,highest, and sum of values in a list

numbers = [1,4,62,43,5,3,23,5,434534,52344,435235,4345,452,74543]

print(min(numbers))
print(max(numbers))
print(sum(numbers))

#use loop to recreate sum function practice


sum_num = 0

for number in numbers:
	sum_num += number

print(sum_num)