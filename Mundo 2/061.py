print('GERADOR DE PA')
print('--' *10)
primeiro_termo = int(input('Diite o 1º termo: '))
razao = int(input('Diite a razao: '))
termo = primeiro_termo
cont = 1
while cont <= 10:
    print('{} --> '.format(termo), end = ' ')
    termo += razao
    cont += 1
print('Fim')