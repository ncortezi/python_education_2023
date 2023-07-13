from random import choice

def make_list(x,y):
	return(list(range(x,y+1)))

numbs = make_list(1,1000)

def lottery():
	numb2 = numbs[:]
	tik_count = 4
	while tik_count > 0:
		draw = choice(numb2)
		print(f"We drew {draw}")
		numb2.remove(draw)
		tik_count -= 1
	print("If you had any of the above, please come collect your prize!")

def user_draw():
	numb = int(input("Choose a number: "))
	if numb in numbs:
		print("You Win!")
	else:
		print("No dice!")


def lottery_count():
	pulled = True
	user_numb = int(input("Pick a number "))
	pull_count = 1
	while pulled:
		pull_numb = choice(numbs)
		print(f"A {pull_numb} has been pulled!")
		if pull_numb == user_numb:
			pulled = False
		else:
			pull_count += 1
	print(f"It took {pull_count} pulls to reach your number!")

	

lottery()

