#Example on Membership operator(in and Not in)

#WAP to accept any of the character from keyboard and print whether it is vowel or consonent
x=input('Enter any character:')
#Method1 using logical operators
#print('It is Vowel') if x=='a' or x=='e' or x=='i' or x=='o' or x=='u' else print('It is Consonent')
#Method2 using Membership operator 'in'
#print('It is Vowel') if x in 'a,e,i,o,u' else print('It is Consonent')
print('It is Consonent') if x not in 'a,e,i,o,u' else print('It is Vowel')