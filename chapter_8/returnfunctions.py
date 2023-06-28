##functions can also "return" a set of values or an operation instead of just printing them to the screen


def format_name(first,last):
	full_name = f"{first.title()} {last.title()}"
	return full_name

user = format_name("jim","murtaugh")

print(user)

