vogais = 'a', 'e', 'i', 'o', 'u'
palavras = 'Astronauta', 'Lanterna', 'Abacaxi', 'Bussola', 'Bola'
for palavra in palavras:
    print(f'As vogais em {palavra} são: ', end='')
    for letra in vogais:
        if letra.lower() in palavra.lower():
            print(f'{letra}', end='')
    print()