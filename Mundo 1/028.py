import random
x=random.randrange(0, 5)
y=int(input('Pensei eum um número entre 0 e 5, advinhe qual é: '))
if x==y:
    print('\033[0;32mParabéns, você acertou!\033[m')
else:
    print('\033[0;31mNão foi desta vez, você perdeu!\033[m')