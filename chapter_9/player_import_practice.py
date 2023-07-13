from random import randint 

class Die:
	def __init__(self,sides):
		self.sides = sides

	def roll(self):
		return(randint(1,self.sides))

six_side = Die(6)

ten_side = Die(10)


def rollout():
	die_choice = input("Which die would you like to use?\n")
	die_count = int(input("How many rolls?\n"))
	while die_count > 0:
		if die_choice == "Six":
			print(six_side.roll())
			die_count -= 1
		elif die_choice == ("Ten"):
			print(ten_side.roll())
			die_count -= 1
		else:
			print("You do not have that die")
			break

rollout()


