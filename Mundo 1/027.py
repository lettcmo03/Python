name=input('Qual é o seu nome completo? ').strip()
novo=name.split()
print('Primeiro nome: {} \nÚltimo Sobrenome: {}' .format(novo[0], novo[-1]))
