#Example on Encapsulation in OOPS
class Subscriber:
    def __init__(self,name,age,mdnno): #Default method/constructor to initialize the object
        self.__name=name
        self.__age=age
        self.__mdnno=mdnno
    def makecall(self): #Method1
        print(self.__name,'is making call')
    def receivecall(self): #Method2
        print(self.__name,'is receiving call')
    def info(self): #Method3
        print(self.__name)
        print(self.__age)
        print(self.__mdnno)
S1=Subscriber('MD',22,8686)
S2=Subscriber('Sam',26,786)
S1.makecall()
S2.receivecall()
S1.info()
S1.name='Shaik'
S1.makecall()
S1.__name='Mohammed'
S1.makecall()