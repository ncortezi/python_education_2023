from random import randint

class Die:
	def __init__(self,sides = 6):
		self.sides = sides

	def roll_die(self,rolls = 1):
		die_face = randint(1,self.sides)
		count = rolls
		while rolls > 0:
			print(f"You rolled a {die_face}")
			return die_face
			rolls -= 1

die1 = Die()

die2 = Die(10)

die3 = Die(20)

enemy_alive = True 

enemy_health = 600

play_attacks = 60

count_attacks = 0

while play_attacks > 0 and enemy_alive:
	attack = die3.roll_die()
	enemy_health -= attack
	play_attacks -= 1
	count_attacks += 1
	if enemy_health <= 0:
		enemy_alive = False
		print(f"You killed the enemy in {count_attacks} hits!")
		break
	else:
		print(f"You did {str(attack)} damage!")
		print(f"The enemy has {enemy_health} HP left!\n")
