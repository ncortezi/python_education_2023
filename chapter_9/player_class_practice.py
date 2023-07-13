class Player:
	def __init__(self,name):
		self.name = name
		self.level = 0

	def say_name(self):
		print(f"My name is {self.name}")

	def lvlup(self):
		self.level +=1

	def show_stats(self):
		print(f"You are level {self.level}")


class Sorcerer(Player):
	def __init__(self,name):
		super().__init__(name)

	def fireball(self):
		print(f"{self.name} casted Fireball!")

class Necromancer(Sorcerer):
	def __init__(self,name):
		super().__init__(name)

	def bone_storm(self):
		print(f"{self.name} casted Bone Storm!")

necro1 = Necromancer("Steve")


sorc1 = Sorcerer("Kalie")

