#WAP to check whether the student has passed or failed based on 3 subject marks and average
#Case1:
''''
Case1:
Enter name:---
Enter Subject1 marks:50
Enter Subject2 marks:50
Enter Subject3 marks:50
Congratulations __ you passed the exam
-------------
Case2:
Enter name:---
Enter Subject1 marks:30
Enter Subject2 marks:30
Enter Subject3 marks:30
__ you Failed
------
Case3:
Enter name:---
Enter Subject1 marks:100
Enter Subject2 marks:50
Enter Subject3 marks:0
 __ you failed in subject(s)
'''
n=input('Enter Name:')
S1=int(input('Enter Subject1 Marks:'))
S2=int(input('Enter Subject2 Marks:'))
S3=int(input('Enter Subject3 Marks:'))
avg=(S1+S2+S3)/3
if avg>=40:
    if S1>=40 and S2>=40 and S3>=40:
        print('Congratulations {} you passed the exam'.format(n))
    else:
        print('{} you Failed in subject(s)'.format(n))
else:
    print('{} you Failed'.format(n))
