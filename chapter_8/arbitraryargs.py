#if we are unsure ahead of time how many arguments a function needs to accept, we can use *
#this will tell Python that there is an arbitrary amount of arguments needed

def pizza(*toppings):
	for topping in toppings:
		print(f"Adding {topping} to your pizza")

pizza("cheese")
print('\n')
pizza("cheese","pepperoni","mushrooms")

#if we want to mix positional and arbititrary arguements, the arb must come LAST in the function
print('\n')
def ice_cream(num_scoops,*toppings):
	print(f"You would like {num_scoops} scoops of ice cream with:")
	for topping in toppings:
		print(f"{topping.title()}")
	print("\nEnjoy!\n")

ice_cream(3,"nuts","fudge","whipped cream")

#sometimes we will want to accept an arb # of arguments but wont know what info will be passed
#in this case, we use ** which allows function to accept as many k-v pairs as callling statement provides
#the double asterisks cause python to create an empty dictionary and to pack k-vs 
def build_user(first,last,**user_info):
	user_info['first_name'] = first
	user_info['last-name'] = last #after this, we can continue to generate k-vs as a dict has already been created
	return user_info

test1 = build_user("Nick","Cortezi",age=30,job="unemployed",eyes="brown")
test2= build_user("Coco","Marshall",location ="New York",hair="blonde",age=34)
print(test1)
print(test2)