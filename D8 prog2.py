'''WAP to accept the list of elements and a key element from the user
and perform linear search and print the O/P as
Element found or not found
l=[2,1,6,7]
key=6
key=3
Element 3 is not found
O/P:Element 6 is found at the position(index)
'''
l=eval(input('Enter the list of elements:')) #To accept list of elements
k=int(input('Enter a key:'))
print(len(l))
for i in range(0,len(l)):
    if k==l[i]:
        print('Element {} found at position {}'.format(k,i))
        break
else:
    print('Element {} is not found'.format(k))