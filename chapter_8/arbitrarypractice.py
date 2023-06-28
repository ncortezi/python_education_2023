#sandwiches

sand1 = ["Cheese","ham","lettuce"]
sand2 = ["ham","tomato","bacon","mustard","mayo"]
sand3 = ["peanut butter","banana"]

def sandwich(*toppings):
	print("Your sandwich will include")
	for topping in toppings:
		print(f"{topping}")

sandwich("cheese","bacon","mustard","ketchup")


#CARS

def car_info(manufacturer,model,**car_info):
	car_info["manufacturer"] = manufacturer
	car_info["model"] = model
	return car_info

car1 = car_info("Honda","CRV",color="Red",condition="New")
car2 = car_info("Toyota","Ford",color="Black",condition="Used",price="$15000")

print(car1)
print(car2)