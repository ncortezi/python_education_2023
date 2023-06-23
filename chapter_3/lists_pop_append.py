#you can add new items to a list using the .append() method

names = ["Coco", "Belle", "Taco"]

print(names)
names.append("Nick")
print(names)

names.append("Carl")
names.append("Cynthia")
print(names)

# we can insert elements into a list using the .insert(x,y) method. x reflects index & y reflects value When a value is inserted, all values will shift one place

"""
the .pop() method removes the last item from a list but stores it for later use
e.g a user unsubscribes from a platform and we want to move them from the active user list
to the unsubscribed user list

"""

users = ["Carl", "Frank", "Kelly"]
non_users = ["Nick", "John", "Alex"]

non_users.append(users.pop())

print(users)
print(non_users)

#popped values can also be stored in their own variables

digits = [1,2,3,4]
final_count = digits.pop()
print(16 + final_count)

#or if we wanted to find the last person to sign up for the software

signups = ["Nick", "Tucc", "Al","Kelly"]
last_signup = signups.pop()
print(f"The most recent member is {last_signup}") #removes Kelly from list and stored as variable
print(f"The most recent member is {signups.pop()}") #removes Al from list as Kelly has been removed
print(signups) #only includes Nick & Tucc

#we can use the pop() method to remove an item from any position in a list by including an index position as an argument

names = ["Jim", "John","Greg"]

removed_name = names.pop(1)

print(names)
print(removed_name)