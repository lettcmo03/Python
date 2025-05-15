r1=int(input('Defina a 1º reta: '))
r2=int(input('Defina a 2º reta: '))
r3=int(input('Defina a 3º reta: '))
if r1+r2<r3 and r2+r3<r1 and r1+r3<r2:
    print('NÃO pode formar um triângulo')
else:
    print('Pode formar um triângulo do tipo: ', end='')
    if r1==r2==r3:
        print('Equilatero')
    elif r1!=r2 and r2!=r3 and r2!=r3:
        print('Escaleno')
    else:
        print('Isosceles')
