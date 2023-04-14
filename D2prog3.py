#Same prog using user define module called math
#import math #importing math module
#import math
import math
r=int(input('Enter a radius value:'))
#vol=4/3*3.14*r*r*r
vol=4/3*math.pi*r*r*r
print('Volume of a sphere is:',vol)