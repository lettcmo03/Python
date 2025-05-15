resposta = int(input('Digite um número de 0 a 20: '))
if 0 <= resposta <= 20:
    num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez'
            'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
    ext = num[resposta]
    print(f'Você digitou o número {ext}')
else:
    resposta = int(input('Digite um número de 0 a 20: '))