baratin = total = mais_mil = item = 0
mais_barato = ''
while True:
    produto = input('Nome do produto: ').capitalize
    valor = float(input('Valor: RS '))
    item += 1
    total += valor
    if item == 1:
        baratin = valor
        mais_barato = produto
    else:
        if valor < baratin: 
            valor = baratin
            mais_barato = produto
    if valor > 1000:
        mais_mil += 1
    mais = input('Gostaria de continuar? [S/N] ').capitalize().strip()
    if mais == 'N':
        break
print(f'O total da sua compra foi de R$ {total}. \n{mais_mil} deles custa mais de R$ 1000. \nO mais barato deles foi {mais_barato} de R$ {baratin}')