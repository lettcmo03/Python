cbf = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional', 'São Paulo', 'Corinthians', 
        'Bahia', 'Cruzeiro', 'Vasco', 'Vitória', 'Atletico Mineiro', 'Fluminense', 'Grêmio', 'Juventude', 
        'Bragantino', 'Athletico PR', 'Criciuma', 'Atlético GO', 'Cuiabá')
for pos, cont in enumerate(cbf[0:5]): #5 primeiros
    print(f'O {pos + 1}º colocado é {cont}')
print('=-'*25)
perdedores = cbf[-4:]
for index, cont in enumerate(perdedores, start=len(cbf)-4): #4 ultimos
    print(f'O {index + 1}º colocado é {cont}')
print('=-'*25)
for time in sorted(cbf): #em ordem alfabética, um por linha
    print(time)
#print(sorted(cbf)) - em ordem alfabetica mas tudo na mesma linha
print('=-'*25)
for pos, time in enumerate(cbf): #achando o fluminense na tupla (ja que nao existe mais chapecoense)
    if time == 'Fluminense':
        print(f'{time} é o {pos + 1}º colocado no Brasileirão')
        break
print('=-'*25)
#print(f'O fluminense esta na {cbf.index('Fluminense') + 1}º posição') - outra maneira de achar o fluminense