print('=' *25)
print('{:^25}'.format('Banco da Let') )
print('=' *25)
valor = int(input('Qual o valor a ser sacado? R$ ')) #descobre quanto vai ser sacado
total = valor #para facil manipulação
ced_atual = 50
total_ced = 0
while True:
    if total >= ced_atual:
        total -= ced_atual
        total_ced += 1
    else:
        if total_ced > 0:
            print(f'Total de {total_ced} cédulas de R$ {ced_atual}')
        if ced_atual == 50:
            ced_atual = 20
        elif ced_atual == 20:
            ced_atual = 10
        elif ced_atual == 10:
            ced_atual = 1
        total_ced = 0
        if total == 0:
            break