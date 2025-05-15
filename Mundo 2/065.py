# maiores e menores / quer continuar / media
mais = 'S'
num = total = maior = menor = soma = media = 0

while mais == 'S':
    num = int(input('Digite um número: '))
    soma += num
    total += 1
    if total == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num 
    mais = input('Quer continuar? [s/n] ') .capitalize() .lstrip()[0]    
media = soma / total
print('Você digitou {} numeros e a média deles foi {}' .format(total, media))
print('\nO maior deles foi: {} \nO menor foi: {}' .format(maior, menor))