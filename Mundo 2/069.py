mais_dezoito = homens = menos_vinte = 0
while True:
    print('-='*20)
    print('CADASTRO DE PESSOAS')
    print('-='*20, end='\n')
    idade = int(input('Idade: '))
    if idade > 18:
        mais_dezoito += 1
    genero = input('Gênero [M / F]: ').capitalize().lstrip()
    if genero == 'M':
        homens += 1
    else:
        if idade < 20:
            menos_vinte += 1
    if genero not in ('M,F'):
        genero = input('Gênero [M / F]: ').capitalize().lstrip()
    mais = input('Quer continuar[S / N]? ').capitalize().lstrip()
    if mais not in ('N,S'):
        mais = input('Quer continuar[S / N]? ').capitalize().lstrip()
    elif mais == 'N':
        break
print('-='*20)
print(f'Foram cadastrados {homens} homens. \nForam também cadastradas {menos_vinte} mulheres abaixo de 20 anos. \nPor fim, {mais_dezoito} são maiores de idade')