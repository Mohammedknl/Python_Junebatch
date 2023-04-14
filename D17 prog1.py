#Example on Functional type of Multithreading
from threading import *
def fun(): #my thread t2
    for i in range(1,6):
        print('I am from child thread t2')
t2=Thread(target=fun) #Creating thread object to execute fun thread
#We have to start the thread
t2.start()
for i in range(1,6):
    print('I am from Main Thread t1')
