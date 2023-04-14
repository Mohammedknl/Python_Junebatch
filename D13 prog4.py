#Example on Default/optional arguments
def add(a,b,c=0):
    return a+b+c
def avg(a,b):
    s=add(a,b)
    return s/2
print(avg(10,20))
print(avg(1,2))
print(add(50,100))
print(add(10,20,30))
