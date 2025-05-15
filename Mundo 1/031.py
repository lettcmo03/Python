viagem=float(input('Qual a distância, em Km, da sua viagem? '))
if viagem<=200:
    print('O valor da sua viagem é: R$ {:.2f}' .format(viagem*0.45))
else:
    print('O vaor da sua viagem é R$ {:.2f}' .format(viagem*0.50))