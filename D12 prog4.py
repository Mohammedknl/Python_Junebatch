#Example on list methods
l=[2,3.14,'hello']
#append method adds the object to the end of the list
l.append(2+3j)
print(l)
#Example on Extend method
a=[1,2.5,'abc']
a.extend('xyz')
print(a)
a.extend((10,11,12))
print(a)
a.insert(3,999)
print(a)
a.remove(999)
print(a)
a.pop()
print(a)
a.pop(2)
print(a)
a.reverse()
print(a)
print(a.count(10))

