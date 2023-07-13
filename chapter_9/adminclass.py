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

class Privileges:
	def __init__(self):
		self.privileges = ["add a post","delete a post","ban a user"]

	def show_privileges(self):
		print(f"This user has permission to do the following:")
		for priv in self.privileges:
			print(f"They can {priv}")

class Admin(User):
	def __init__(self,first_name,last_name,age,location):
		super().__init__(first_name,last_name,age,location)
		self.privileges = Privileges()

admin1 = Admin("Nick","Cortei",12,"Baltimore")

admin1.privileges.show_privileges()

