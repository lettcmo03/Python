import random
x='Sarah', 'Liz', 'Luke', 'Peter'
c1=random.choices(x, k=1)
c2=random.choices(x, k=1)
c3=random.choices(x, k=1)
c4=random.choices(x, k=1)
print('A ordem vai ser \n1º {} \n2º {} \n3º {} \n4º {}' .format(c1, c2, c3, c4))