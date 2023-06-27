#if we want a while loop to return to the top without either quitting or running the full block, we use continue

current_number = 0

while current_number < 10:
	current_number += 1
	if current_number % 2 == 0:
		continue #if the number is even (modulo 0), the block restarts and the number is not printed
	print(current_number)