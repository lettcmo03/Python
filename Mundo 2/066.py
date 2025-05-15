# crie um programa que leia varios núers inteiros pelo teclado. O programa so vai parar quando o usuário digtar o valor 999, que é a condição de 
# parada. no final mostre quantos numeros doram digitados e qual foi a soma entre eles
# (desconsiderando o flag)

num = cont = soma = 0
while True:
    num = int(input('Digite um número (999 para encerrar): '))
    if num != 999:
        cont += 1
        soma += num
    else:
        break
print(f'A soma dos {cont} números é {soma}!')