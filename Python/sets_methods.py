s = {11,15,4,8,4,1,12,65,32,95}
print(s)
s.add(18)
print(s)
s.remove(11)
print(s)
#s.pop()  # remove arbitary number
#print(s)

s1 ={14,11,18,20,2,4,65,45}
print(s.union(s1),) #Union

print(s.intersection(s1)) #Intersection

print(s.difference(s1))  # same s - s1

print(s.symmetric_difference(s1))   #Symmetric Difference

print(s.issubset(s1)) # if s1 is subset of s (TRUE/FALSE)

print(len(s))    #length 