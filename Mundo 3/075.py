par =  0
num = tuple(int(input('Digite um número: ')) for x in range(4)) #cria a tupla ja com o int(input()) entrelaçado
print('='*15)
print(num)
print('='*15)
if num.count(9) == 1: #conta quantas vezes apareceu o número 9 e imprime o resultado
    print(f'O número 9 apareceu {num.count(9)} vez')
else:
    print(f'O número 9 apareceu {num.count(9)} vezes')
print('='*15)
if num == 3:
    print(f'A primeira vez que o número 3 foi digitado foi na posição {num.index(3) + 1}')
else:
    print('O número 3 não foi digitado')
print('='*15)
for p in num:
    if p % 2 == 0:
        p = tuple
print(f'Os números pares são: {p}')