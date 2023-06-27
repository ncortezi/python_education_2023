#we can nest multiple dictionaries in a list or a list of items as a value in a dictionary

alien_0 = {'color':'green', 'speed':'fast'}
alien_1 = {'color':'yellow','speed':'slow'}
alien_2 = {'color':'pink','speed':'fast'}

aliens = [alien_0,alien_1,alien_2]

for alien in aliens:
	print(alien)


alien_bugs = []

for alien_number in range(30):
	new_alien = {'speed':'fast','color':'blue'}
	alien_bugs.append(new_alien)

for alien in alien_bugs[:5]:
	print(alien)

print(f'Total number of aliens is {len(alien_bugs)}\n')

#we can also nest a list as a value in a dictionary

pizza = {
	'crust':'thick',
	'toppings':['pepperoni','cheese','mushrooms'],
}

for topping in pizza['toppings']:
	print(f"Adding {topping} to your pie")