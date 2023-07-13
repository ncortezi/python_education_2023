#if the class we are writing is a specialized version of another class, we can use inheritance
#the inheriting class takes on the attributes and methods of first class
#the first class is the Parent class, the second is the Child class

class Car:
	"""A Simple attempt to represent a car"""

	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
		#we can define instance attributes w/o it being passed in the parameters
		#these are defined in the init method where we assign a default value

	def get_descriptive_name(self):
		long_name = f"{self.make} {self.model} {self.year}"
		return long_name

	def read_odometer(self):
		print(f"This car has been driven {self.odometer_reading} miles")

	def increment_odometer(self,miles):
		'''Adds the given amount to the odometer reading'''
		self.odometer_reading += miles

#when creating a child class, we usually want to call the __init__methods of the frist class

class ElectricCar(Car):
	#class ChildClass(ParentClass)
	""" Represents aspects of a car specific to electric vehicles"""

	def __init__(self,make,model,year):
		super().__init__(make,model,year)
		#super() functions allows us to call a method from parent class
		#when it is in init, it attaches all behaviors & functions from the Parent class
		self.electric_battery_size = 1000
		#when it is just self, these methods and attribute will only pertain to child class

	def get_battery(self):
		print(f"This model has a {self.electric_battery_size}-kHz battery")


