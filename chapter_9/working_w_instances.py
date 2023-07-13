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

	def update_odometer(self,miles):
		'''Allows user to set mileage'''
		if miles >= self.odometer_reading:
			self.odometer_reading = miles
		else:
			print("You can't roll back an odometer!")

	def increment_odometer(self,miles):
		'''Adds the given amount to the odometer reading'''
		self.odometer_reading += miles

my_new_car = Car("Porsche","911","2015")

print(my_new_car.get_descriptive_name())

my_new_car.read_odometer()

#the simplest way to modify attribute value is by accessing directly through an instance
#we can also use a method built within the class (added above)

my_new_car.odometer_reading = 34

my_new_car.read_odometer()

my_new_car.update_odometer(45)

my_new_car.read_odometer()

my_new_car.increment_odometer(30)

my_new_car.read_odometer()

