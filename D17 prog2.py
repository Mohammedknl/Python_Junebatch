#Example on Multithreading using OOPS style
from threading import *
#Thread class is parent class and Mythread class is a child class
class Mythread(Thread):
    def run(self):
        for i in range(1,6):
            print('I am',current_thread().getName())
t2=Mythread()
t2.setName('MD')
t2.start()
for i in range(1,6):
    print('I am',current_thread().getName())