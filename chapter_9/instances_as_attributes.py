#if we find our list of attributes and methods becoming too lengthy in a class, we
#can see if part of one class can be written as a separate class
#in this case, we see that a lot of attr. & methods in ElecCar are about the battery
#so we move those attributes and methods to a separate class called Battery

class Car:
	"""A Simple attempt to represent a car"""

	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		long_name = f"{self.make} {self.model} {self.year}"
		return long_name

	def read_odometer(self):
		print(f"This car has been driven {self.odometer_reading} miles")

	def increment_odometer(self,miles):
		'''Adds the given amount to the odometer reading'''
		self.odometer_reading += miles

class Battery:
	#simple attempt to represent an electric car battery

	def __init__(self, battery_size=75):
		#initialize battery attributes
		self.battery_size = battery_size

	def describe_battery_size(self):
		#print a statement describing battery size
		print(f"This car has a {self.battery_size}kHz battery")

	def get_range(self):
		#print statement about range the battery size provides
		if self.battery_size <100:
			range = 260
		else:
			range = 450
		print(f"This car's battery has a range of {range} miles")

	def upgrade_battery(self):
		if self.battery_size < 100:
			self.battery_size = 100

class ElectricCar(Car):
	""" Represents aspects of a car specific to electric vehicles"""

	def __init__(self,make,model,year):
		#initialize electric car attributes
		super().__init__(make,model,year)
		self.battery = Battery(50)
		#This tells Python to create a Battery instance with 100 as the size, would be 75 as default if left empty
		#Every created instance of an ElectricCar will also create a Battery instance

my_tesla = ElectricCar("Tesla","S","1999")

my_honda = ElectricCar("Honda","CSV","1999")

print(f"{my_honda.battery.describe_battery_size()}")

my_honda.battery.upgrade_battery()

print(f"{my_honda.read_odometer()}")
#we then need to use dot notation to go from the ElectricCar instance to the associated Battery instance


