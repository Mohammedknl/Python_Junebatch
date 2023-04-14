#Example on List comprehension
#WAP to find the common elements from list x and list y
x=[1,2,3]
y=[2,3,4]
#z=[]
t=[i for i in x for j in y if i==j]
print('Common elements with list comprehension is:',t)