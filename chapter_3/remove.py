#if we do not know the index position but we do know the value we can use .remove(x)

names = ["Nick", "Chris","Carly","Max"]

names.remove("Nick")

print(names)

# we can also use the remove() method like pop() to work with the removed value

cars = ["Bugatti", "Kia", "Honda"]

too_pricey = "Bugatti" #we assign the value to the variable
print(cars)

cars.remove(too_pricey) #we ask the list to remove the variable & therefore the value associated

print(cars)
print(f"Unfortunately, the {too_pricey} is outside my price range")



