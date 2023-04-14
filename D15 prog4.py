#Example on Inheritance in OOPS
class Subscriber: #Parent class
    def makecall(self):
        print('Subscriber is making call')
    def receivecall(self):
        print('Subscriber is receiving call')
class WLS(Subscriber): # Child class1
    def sendsms(self):
        print('Subscriber is sending SMS')
class BBS(WLS): #child class2
    def browse(self):
        print('Subscriber is browsing interet')
b=BBS()
b.receivecall()
b.sendsms()
b.browse()
