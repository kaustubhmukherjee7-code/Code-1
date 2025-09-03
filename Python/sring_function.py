name = input("Enter the name : ")

print (type(name))

# To find the length of the name
a = len(name)
print(a)

 #To find the start, end is given letter
b = name.endswith("h")  # Point to be noted it's case sensetive. It gives differnt result on small and capital letter
print(b)

c = name.startswith("K")
print(c)

 # It capatalize/lower first letter 
d = name.capitalize()
d1 = name.lower()
print(d)
print(d1)

# For replace any string

name1 = input("Write Replace name: ")
e = name.replace("kaustubh",name1)
print(e)

# To remove front or back blank space

f = name.strip()
print(f)

#Swap lower and upper

g = e.swapcase()
print(g)