#Tuple wit immutable
t=(1,2,3)
print('id of object before changing',id(t))
print('Tuple of elements before changing:',t)
t+=(4,)
print('id of tuple object after changing:',id(t))
print('Tiple of elements aftetr changing:',t)