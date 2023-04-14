#WAP to remove the the characters of odd index values from a string
#I want to print only the even index values characters
'''
I/P:'0123456789'
O/P:02468
'''
s=input('Enter the string:')
print(len(s))
x='' #Empty variable to store the result
for i in range(0,len(s)): #range(0,10)
    if i%2==0:
        x=x+s[i] #It concatinate the index value to the empty string x
print('Output is:',x)