def add(a,b):  # This add func is available for Garbage collection.
    return a+b
def avg(a,b):
    s = add(a,b)
    return s/2
def add(a,b,c):  # It overwrites with existing add func to use
    return a+b+c
print(add(2,3,4))
print(add(10,20,30))
print(avg(5,5))
