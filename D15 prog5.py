#Example on Method Overriding and Inheritance
class parent:
    def property(self):
        print('10 lakhs from parents without overriding')
    def marriage(self):
        print('Marry with xyz from parents')
class child(parent):
    def marriage(self):

        print('Marry with abc from method overriding')
c=child()
c.property()
c.marriage()
