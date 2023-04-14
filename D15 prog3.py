#Example prog on without Inheritance
class Subscriber: #Class 1
    def makecall(self):
        print('Subscriber is making call')
    def receivecall(self):
        print('Subscriber is receiving call')
class WLS: # class 2
    def makecall(self):
        print('Subscriber is making call')
    def receivecall(self):
        print('Subscriber is receiving call')
    def sendsms(self):
        print('Subscriber is sending SMS')
class BBS: #class3
    def makecall(self):
        print('Subscriber is making call')
    def receivecall(self):
        print('Subscriber is receiving call')
    def sendsms(self):
        print('Subscriber is sending SMS')
    def browse(self):
        print('Subscriber is browsing interet')
s=Subscriber()
s.makecall()
s.receivecall()
w=WLS()
w.sendsms()
w.makecall()
b=BBS()
b.browse()