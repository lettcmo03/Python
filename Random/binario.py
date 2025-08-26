num = 14 # num que eu quero transformar 
restos = [] # lista que armazena os resto da divisao
while num > 0: 
    restos.append(num % 2) # adiciona os restos (formula em parentesis) da divisão na lista
    num = num // 2 # configura que o dividendo sera sempre igual ao quoeficiente anterior, desde que não seja 0


binario = restos[::-1] # inverte a ordem da lista
print(binario) # mostra o resultado na tela