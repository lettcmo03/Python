# crie um programa que leia o sexo de uma pessoa (m ou f), caso a digitação esteja errada, tente novamente
g = ''
while g not in ['F', 'M']:
    g = str(input('Genero [F / M]: ')).strip().upper()
if g == 'F':
    print('Gênero Feminino registrado com sucesso!')
elif g == 'M':
    print('Gênero Masculino registrado com sucesso!')
