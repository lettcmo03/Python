# crie um programa que mostre a tabuada de vários números, um de cada vez para cada valor digitado pelo usuário o prgrama sera interrompido quando
# o numero digitado for negativo
num = cont = 0
while True:
    print('-'*20) 
    num = int(input('Digite um numero e veja sua tabuada: '))
    print('-'*20)
    cont = 1
    if num > 0:
        for i in range(num, num * 11, num):
            print(f' {num} x {cont} = {i}')
            cont +=1
    else:
        break
print('Fim')