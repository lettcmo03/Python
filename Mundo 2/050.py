sum = 0
cont = 0
for c in range(1,7):
    num = int(input('Digite o {} valor: ' .format(c)))
    if num % 2 == 0:
        sum = sum + num
        cont = cont + 1
print('você informou {} numeros pares e a soma deles foi {}' .format(cont, sum))