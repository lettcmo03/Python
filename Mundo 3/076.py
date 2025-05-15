print('-'*40)
print('TABELA DE PREÇOS')
print('-'*40)
precos = ('Barraca', 90, 'Cadeira', 154.5) #criei a tupla
for x in range(0, len(precos), 2): #separei quem era preco e que era produto, lendo a tupla puando sempre de 2 em 2
    produto = precos[x]
    valor = precos[x + 1] #aqui eu disse que o valor era sempre depois do nome do produto
    print(f'{produto} ....................... R$ {valor:.2f}')
print('-'*40)

