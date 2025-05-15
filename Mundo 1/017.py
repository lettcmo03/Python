import math 
c1=int(input('cateto adjacente: '))
c2=int(input('cateto oposto: '))
h=int(math.pow(c1, 2)+math.pow(c2, 2))
print('a hipotenusa é {}.' .format(math.sqrt(h)))
