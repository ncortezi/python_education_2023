enemy_health = 20

hits = 1

while hits > 0:
	damage = 10
	print(f"You did {damage} damage!")
	enemy_health -= damage
	hits -= 1

if enemy_health <= 0:
	print("You've defeated the enemy!")
else:
	print(f"The enemy has {enemy_health} HP left!")