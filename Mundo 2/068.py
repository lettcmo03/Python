import random
print('-='*10, '\nVAMOS JOGAR PAR OU IMPAR')
print('-='*10)
hcn = 0 # escolha do numero do humano
rcn = 0 # escolha do numero do computador
hc = 0 # escolha do humano
rc = 0 # escolha do computador
vic = los = soma = 0
while True:
    hcn = int(input('Escolha um número: '))
    hc = input('Par ou Impar [P/I]? ').capitalize().lstrip()[0]
    rcn = random.randint(1,10)
    rc = random.choice('P''I').capitalize()
    soma = hcn + rcn
    if (soma % 2) == 0:
        resultado = 'P'
        if resultado == hc:
            print(f'Você jogou {hcn} e o computador jogou {rcn}. Total de {soma}. DEU PAR!\n', '-'*20, '\nVocê venceu!\n')
            print('Vamos jogar novamente...')
            print('-='*10)
            vic += 1
        else:
            print(f'Você jogou {hcn} e o computador jogou {rcn}. Total de {soma}. DEU PAR!\n', '-'*20, '\nVocê perdeu!')
            los += 1
    else:
        resultado = 'I'
        if resultado == hc:
            print(f'Você jogou {hcn} e o computador jogou {rcn}. Total de {soma}. DEU IMPAR!\n', '-'*20, '\nVocê venceu!\n')
            print('Vamos jogar novamente...')
            print('-='*10)
            vic += 1
        else:
            print(f'Você jogou {hcn} e o computador jogou {rcn}. Total de {soma}. DEU IMPAR!\n', '-'*20, '\nVocê perdeu!')
            los += 1
    if los > 0:
        break
print(f'GAME OVER! Você venceu u total de {vic} vezes seguidas!')