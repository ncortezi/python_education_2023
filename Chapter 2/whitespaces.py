print("Python")
print("\tPython") 
# \t tabs out the line

print("Python \nJava \nC++\n")
# \n starts new line

# \n & \t can be combined like below

print("Names: \n\tFrank \n\tSteve \n\tAlex\n")

#method .rstrip() will strip white space to right of string, lstrip to left, and strip to both

name = "   Nick Cortezi    "
print(name.rstrip())
print(name.lstrip()) #note there are still white spaces 
print(name.strip())
