#WAP to perform addition of two numbers using comma operator
#By using String Modulo operator and by using placeholder method
a=int(input('Enter value of a:'))
b=int(input('Enter value of b:'))
c=a+b
#I way using comma operator: Addition of 10 and 20 is 30
print('Addition of',a,'and',b, 'is',c)
#II way using String Modulo operator/Format specifier:
print('Addition of %d and %d is %d'%(a,b,c))
#III way using Place holder method:
print('Addition of {} and {} is {}'.format(b,a,c))

#70 percent of 100 is 70