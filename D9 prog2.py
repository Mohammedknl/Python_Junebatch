#Nested loops

'''
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
'''
n= int(input('Enter n value:'))
for i in range(1,n+1): #range(1,6)--1,2,3,4,5
    for j in range(1,i+1): #range(1,3)--1,2
        print(i,end=' ')
    print()