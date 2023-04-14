'''
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1
'''
'''row=int(input('Enter no of rows:'))
for i in range(1,row+1): #W.R.T to rows range(1,6)---1,2,3,..5
    for j in range(i,0,-1):#range(2,0)
        print(j,end=' ')
    print()
   '''
for i in range(1,6):
    for j in range(i,0,-1):
        print(j,end=' ')
    print()



