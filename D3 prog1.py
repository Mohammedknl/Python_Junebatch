'''
WAP to alculate Toctal salary of Rahul
Rahul's basic salary is taken as an input through the keyboard
His D.A is 50% of his basic salary
His H.R.A is 30% of his Basic salary

'''

#section1:I/P
#If basic salary is 100 ---------I/P
bs=int(input('Enter Rahul basic salary:'))
#Section2: Logic
#D.A=50/100*basic salary=50
#H.R.A=30/100*basic sal=30
da=bs*50/100
hra=bs*30/100
Ts=int(bs+da+hra)
#Section3:O/P
#Total sala=Basic+D.A+H.R.A =180----O/P
print('D.A is:',da)
print(type(da))
print('HRA is:',hra)
print(type(hra))
print('Total salary of Rahul is:',Ts)

print(type(Ts))