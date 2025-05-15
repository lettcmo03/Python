#ler o nome, 
#idade e 
#sexo de 4 pessoas, 
#diga: media de idade, homem mais velho, mulher abaixo de 20 anos ☻
menor_vinte = media = mais_velho = cont = 0
for n in range(1,5):
    print('--- {}ª PESSOA ---' .format(n))
    name = input('Nome: ').capitalize()
    age = int(input('Idade: '))
    if n == 1:
        mais_velho = age
    cont += 1
    media = (age)/ cont
    sex = input('Gênero (M) / (F): ').upper()
    if sex == 'F':
        if age < 20:
            menor_vinte += 1
    if sex == 'M':
        if age > mais_velho:
            print(name, age)
if menor_vinte == 1:
    print('Ao todo, {} mulher tem menos de 20 anos' .format(menor_vinte))
else:
    print('Ao todo, {} mulheres tem menos de 20 anos' .format(menor_vinte))
