a = {1, 4, 2.4, 'aaa', 'abc', 9, 2}
b = set([1 ,4 ,3 , 'abc', 87])
print(a)
print(b)

c = set()
print(c)

print(dir())

#Finding the length of a Set
print(len(a))

#Accessing Elements of a Set
for x in a:
    print(x)

#Adding Elements to a Set
c.add(3)
print(c)

c.update([2, 'abc', 3])
print(c)

#Removing Elements from a Set
a.remove(2.4)
print(a)

#a.remove(6) #KeyError: 6
print("Before Delete : ", b)
b.discard(3)
print("After Delete : ", b)
print("Before Delete : ", b)
b.discard(90)
print("After Delete : ", b)

print(a.pop())
print(a)

#Union of Sets
print(a|b)
print(a.union(b))
print(a|b|c)
print(a.union(b, c))

#Intersection of Sets
print(a&b)
print(a.intersection(b,c))

#Difference of Sets
print(a-b)
print(b-a)
print(a.difference(c))
print(a.difference(b,c))

#Frozen Sets
d = frozenset(a)
print(d)

#d.add(3) #AttributeError: 'frozenset' object has no attribute 'add'


a = {'10', '20', '30', '40'}
b = {'30', '60'}
u = a|b
print(u)
i = a&b
print(i)
d = a-b
print(d)
sd = a^b
print(sd)

