# criar um programa que leia qualquer numero, ao ler 999, pare e some os anteriores (desconsiderando o 999)
num = soma = cont = 0
while num != 999:
    num = int(input('Digite quaquer numero (999 para parar): '))
    soma += num
    cont += 1
print('Você digitou {} números e a soma deles é: {}' .format(cont, soma - 999))