#Example on Compile time polymorphism/Method Overloading
#@ methods with same name and with difff parameters is called Method overloading/Compile time Polymorphism
class Average:
    def avg(self,*args):
        s=0
        for i in args:
            s=s+i
        return s/len(args)
x=Average()
print(x.avg(2,4))
print(x.avg(1,2,3))
print(x.avg(1,2,3,4))