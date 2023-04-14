#Example on OOPS concept
class Subscriber: #Class name is Subscriber
    def makecall(self): #Method1
        print(self.name,'is making call')
    def receivecall(self): #Method2
        print(self.name,'is receiving call')
    def info(self): #Method3
        print(self.name)
        print(self.age)
        print(self.mdnno)
#Step2:Creating an object of the class
S1=Subscriber() #Creating an object of the Subscriber class
print(type(S1))
S1.name='Seema'
S1.age=25
S1.mdnno=9866
S1.receivecall()
S1.makecall()
S2=Subscriber()
S2.name='Mohammed'
S2.age=30
S2.mdnno=7864
S2.makecall()
S2.info()
S1.info()