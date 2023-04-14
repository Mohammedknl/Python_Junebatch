#I/P:Hello
#O/P:HHeelloo
x=input('Enter a string:')
y=''#Creating an empty string
for i in x: #i=H,e,l,l,o
    y+=i*2 #y+ means add to empty variable y
print('Output=',y)