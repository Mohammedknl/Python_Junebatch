#Example on Exception handling with specialised and generalised exception block of codes
try:
    l=[] #Created an empty list
    print(l[0])
    #a=int(input('Enter a value:'))
    #b=int(input('Enter b value:'))
    #c=a/b
    #print('printing Division without exception is:',c)
except ZeroDivisionError as e:
    print('This is the specialized exception message:',e)
except IndexError as f:
    print('Specialized message from f is:',f)
print('Last line of the program')
