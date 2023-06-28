#we can store & import functions by using modules 
#modules are .py files containing functions & values that can be used across multiple programs

import pizza_module #imports the entire module from the directory

pizza_module.make_pizza(16,"cheese")
#module name - function name

from toppings import top_off #imports specific functions from a module

top_off("Cheese","Pepperoni")
#only need the function name


#we can use "as" to import a function and assign an alias. We can also do this with modules

from toppings import greet_customer as gc

gc("Nick Cortezi")

#if we want to import all functions from a module, we use asterisks (not best practice)
#from toppings import * 