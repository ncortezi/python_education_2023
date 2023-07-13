class Restaurant:
	def __init__(self,name,cuisine_type="American"):
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


class IceCreamStand(Restaurant):
	def __init__(self,name,cuisine_type,flavors):
		super().__init__(name,"Ice Cream")
		self.flavors=flavors
	def show_flavors(self):
		print("We have the following flavors:")
		for flavor in self.flavors:
			print(f"{flavor}")
	def describe_restaurant(self):
		print(f"{self.name} is an ice cream stand")

stand1 = IceCreamStand("Frosty's","Ice Cream",["Strawberry","Honey","Chocolate"])
rest1 = Restaurant("Michael's","American")

stand1.describe_restaurant()
rest1.describe_restaurant()

stand1.show_flavors()