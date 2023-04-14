#Example prog on Logical operators
#WAP to accept age and percentage of a candidate and print whether he is qualified or not
#if age<=25 and percentage>=75 then i have to print he is qualified
age=int(input('Enter age:'))
per=float(input('Enter percentage:'))
#Method1 using conditional operator in a single line
#print('She is qualified') if age<=25 or per>=75 else print('She is not qualified')
#Method2 using Indentation
if age<=25 and per>=75:
    print("He is qualified")
else:
    print("He is not qualified")