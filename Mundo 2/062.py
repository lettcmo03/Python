print('Gerador de PA 3.0') #I HATE THIS FUCKING THING
print('=' * 20)
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: ')) 
termo = primeiro
cont = 1
total = 0
continuar = 10
while continuar != 0:        
    total = total + continuar
    while cont <= total: 
        print('{} --> ' .format(termo), end = ' ')
        termo += razao
        cont += 1
    print('PAUSA')
    continuar = int(input('Quantos termos a mais você gostaria de ver? '))
print('FIM')
print('A PA foi finalizada com {} termos mostrados.' .format(cont))