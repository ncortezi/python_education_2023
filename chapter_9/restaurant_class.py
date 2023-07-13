#restaurant

class Restaurant:
	def __init__(self,name,cuisine_type):
		self.name = name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print(f"{self.name} serves {self.cuisine_type} food")

	def open_restaurant(self):
		print(f"{self.name} is now open!\n")

	def set_number_served(self,num_served):
		self.number_served = num_served

	def increment_number_served(self,num_served):
		self.number_served += num_served

restaurant = Restaurant("Taco Bell","Mexican")
restaurant_2 = Restaurant("Pizza Hut","Italian")
restaurant_3 = Restaurant("McDonald's","American")

restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.set_number_served(10)

print(restaurant.number_served)

restaurant.increment_number_served(34)

print(restaurant.number_served)