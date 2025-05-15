import random
aleatorio = tuple(random.randint(1,15) for x in range(5)) #cria a tupla e gera os numeros 
org = sorted(aleatorio)
print(aleatorio)
print(f'O menor é {org[0]} e o maior é {org[4]}')