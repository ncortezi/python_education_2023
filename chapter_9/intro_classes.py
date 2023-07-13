#classes represent real-world things & situations from which we can instantiate objects
#when you create an object, it automatically has all general behaviors and attributes from the parent class
#methods are definied as functions created & associated with a certain class

class Dog: 
	"""A simple attempt to make a dog"""
	def __init__(self,name,age):
		"""initiate name and age attributes"""
		self.name = name
		self.age = age

	def sit(self):
		'''simiulate a dog sitting in response to a command'''
		print(f"{self.name} is now sitting.")

	def roll_over(self):
		'''simulate rolling over response to a command'''
		print(f"{self.name} rolled over!")

"""
	the __init__() method is a special method that pythan automatically
	runs when we create a new instance based on a class

	the self parameter is required and must come before any other attributes
	this is passed automatically when we create an instance
	
	we use self to attribute behaviors and variable back to the instance created
	so "self.name = name"
		1) takes parameter associated with name and assigns it as variable name
		2) attaches the variable to the instance being created

	with roll_over(self)
		1) we include self when defining the method, but will not need to pass it for an instance
		2) this is just to say that any instance of Dog class will be able to action these functiosn
	
	By using "self" within the methods, you can differentiate between instance variables specific 
	to the object and local variables within the method. It helps maintain the state of the object
	and enables object-specific behavior and data access in object-oriented programming.

"""

#making an instance of the class

my_dog = Dog('Willie',6)
#variable = class(x,y)
#we use dot notation to access the functions & attributes in the instance
print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old")

my_dog.sit()
my_dog.roll_over()