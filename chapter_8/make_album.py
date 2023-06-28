def make_album(artist,title,tracks=None):
	if tracks:
		album = {'artist':artist,'title':title,'tracks':tracks,}
		return album 
	else:
		album = {'artist':artist,'title':title,}
		return album

active = True
album_collection = []


while active: 
	artist = input("\nWhat artist would you like to add? (Press q to quit) \n\n")
	if artist == 'q':
		active = False
		break
	album = input("\nWhat album would you like to add?\n\n")

	new_album = make_album(artist,album)
	album_collection.append(new_album)
	print(f"\nAdding {album} by {artist}\n")

print("\n---YOUR DISCOGRAPHY---\n")
for album in album_collection:
	print(album)
print('\n')
