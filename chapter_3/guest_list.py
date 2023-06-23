#initial list of guests

dream_guests = ["Matt Healy", "Thom Yorke", "Stephen King"]

print(f"Hello {dream_guests[0]} I'd love if you could join me for dinner")
print(f"Hello {dream_guests[1]} would you be free to attend a dinner this weekend")
print(f"Hello {dream_guests[2]} please let me know if you would be free this Friday for a meal")
print("\n")

#someone can't make it, we have to invite someone else and remove the original person

print(f"Unfortunately, {dream_guests[1]} cannot make it \n")
dream_guests[1] = "Jalen Hurts"

print(f"Hello {dream_guests[0]} are you still available to join for dinner?")
print(f"Hello {dream_guests[1]}, it turns out we had a last minute backout, are you free to join?")
print(f"Hello {dream_guests[2]}, please let me know if you will still be in attendance\n")

#more space, adding new invites using insert & append

print(f"Hello {dream_guests[0]}, {dream_guests[1]}, {dream_guests[2]}, we have more space and will be inviting more folks!\n")

dream_guests.insert(0,"Alec Baldwin")
dream_guests.insert(2,"Harry Hart")
dream_guests.append("Mookie Bettss")

print(f"Please come to my party {dream_guests[0]}")
print(f"Please come to my party {dream_guests[1]}")
print(f"Please come to my party {dream_guests[2]}")
print(f"Please come to my party {dream_guests[3]}")
print(f"Please come to my party {dream_guests[4]}")
print(f"Please come to my party {dream_guests[5]}\n")

print("I'm sorry, it looks like we only have space for two!\n")

#turns out not enough space, removing uninvited with .pop() and then clearing list with del

print(f"Sorry {dream_guests.pop()} but we can't accommodate you")
print(f"Sorry {dream_guests.pop()} but you'll have to miss this one")
print(f"Sorry {dream_guests.pop()}, see you next time")
print(f"Sorry {dream_guests.pop()} but have a great night\n")

print(f"See you tonight {dream_guests[0]}")
print(f"See you tonight {dream_guests[1]}\n")

del dream_guests[0]
del dream_guests[0]

print(dream_guests)

