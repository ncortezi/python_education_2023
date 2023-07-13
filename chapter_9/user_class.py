
class User:
	def __init__(self,first_name,last_name,age,location):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.location = location
		self.login_attempts = 0

	def describe_user(self):
		print(f"{self.first_name} {self.last_name} is {self.age} years old and lives in {self.location}")

	def greet_user(self):
		print(f"Hello {self.first_name} {self.last_name}!")

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0

user_1 = User("Nick","Cortezi",30,"New York")
user_2 = User("Jared","Sullivan",29,"Baltimore")
user_3 = User("John","Bradley",32,"Scranton")

user_1.increment_login_attempts()
user_1.increment_login_attempts()

print(f"{user_1.login_attempts}")

user_1.reset_login_attempts()

print(f"{user_1.login_attempts}")