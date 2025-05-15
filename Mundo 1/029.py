vm=int(input('Qual a vlocidade do carro? '))
multa=(vm-80)*7
if vm>80:
    print('Você foi multado em R$ {}' .format(multa))
else:
    print('Tudo tranquilo')