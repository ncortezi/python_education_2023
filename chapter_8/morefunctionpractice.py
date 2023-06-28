#CITY NAMES

def city_country(city,country):
	return(f"{city.title()}, {country.title()}")

city1 = city_country("paris","france")
city2 = city_country("berlin","germany")
city3 = city_country("ontario","canada")

cities = [city1,city2,city3]

for city in cities:
	print(city)
print('\n')

#ALBUMS

def make_album(artist,title,tracks=None):
	if tracks:
		album = {'artist':artist,'title':title,'tracks':tracks,}
		return album 
	else:
		album = {'artist':artist,'title':title,}
		return album

album1 = make_album("Radiohead","Ok Computer",21)
album2 = make_album("Sigur Ros","Aegits Byrnum")
album3 = make_album("Modest Mouse","Lonesome Crowded West",21)

print(album2)