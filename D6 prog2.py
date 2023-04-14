#WAP to accept Marks of 3 subjects and display the grade based on the avg as below
'''
if the avg is >70 then print GradeA
if the avg is between 60 &70 then print GradeB
if the avg is in between 50 & 60 then print Grade C
if the avg is in between 40 & 50 then print Grade D
If the avg is <40 then Grade E
'''
S1=int(input('Enter Subject1 Marks:'))
S2=int(input('Enter Subject2 Marks:'))
S3=int(input('Enter Subject3 Marks:'))
avg=(S1+S2+S3)/3
print(avg)
if avg>=70:
    print('Grade A')
elif avg>=60:
    print('Grade B')
elif avg>=50:
    print('Grade C')
elif avg>=40:
    print('Grade D')
else:
    print('Grade E')