#Example2 on OOPS
class Subscriber:
    def __init__(self,name,age,mdnno): #Default method/constructor to initialize the object
        self.name=name
        self.age=age
        self.mdnno=mdnno
    def makecall(self): #Method1
        print(self.name,'is making call')
    def receivecall(self): #Method2
        print(self.name,'is receiving call')
    def info(self): #Method3
        print(self.name)
        print(self.age)
        print(self.mdnno)
S1=Subscriber('Seema',22,8686)
S1.makecall()
S2=Subscriber('MD',30,9866)
S2.receivecall()
S3=Subscriber('imran',21,97485)
S3.info()