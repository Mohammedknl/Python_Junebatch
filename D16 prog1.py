#Example on Exception handling
#Without Exception handling
a=int(input('Enter a value:'))
b=int(input('Enter b value:'))
try:
    c=a/b
    print('Division of a and b is:',c)
except ZeroDivisionError as e:
    print('This is message from except object',e)
print('Division printed normally without terminating')