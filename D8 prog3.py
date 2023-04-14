#Flow control statement Else with loop
for i in range(1,11):
    if i==10:
        break
    print(i,end=' ')
else:
    print('\nI am From Else block')
print('\nI am outside of blocks')#