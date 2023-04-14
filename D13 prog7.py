#Function Overloading in python
def add(*a): #* represents variable length
    s=0
    for i in a:
        s=s+i
    return s
def avg(*a):
    s=add(*a)
    print(len(a))
    return s/len(a)
#Calling the functions
print(add(1,2,3))
print(add(1))
print(avg(10,20))
print(avg(10,20,30))