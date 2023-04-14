#Example on List and Tuple Mutability
#List is Mutable data structure(cahnaged)
l=[1,2,3,4]
print('Id of object l before changing',id(l))
print('List of elements before changing is:',l)
l+=[5] #adding element 5 in to the list l
print('Id of object l after adding canging is:',id(l))
print('List of elememnts after changing is:',l)

