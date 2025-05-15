mome_produto = 'Barraca Mor'
valor_real = 90.00
pag = input('Qual será a forma de pagamento Débito (d), Crédito (c), Dinheiro ou Pix (ep), Parcelado em 2x (2p), Parcelado em 3x (3p)? ').lower()
if pag == 'ep':
    print('Darei 10 % de desconto.', end =" ")
    print('Seu total ficou: {}' .format(valor_real - ((10 / 100) * valor_real)))
elif pag == 'd':
    print('Darei 5 % de desconto.', end =" ")
    print('Seu total ficou: {}' .format(valor_real - ((5 / 100) * valor_real)))
elif pag == 'c':
    print('Infelizmente não poderei te dar desconto.', end =" ")
    print('Seu total ficou: {}' .format(valor_real))
elif pag == '2p':
    print('Haverá um acrescimo de 20 %.', end =" ")
    print('Seu total ficou: {}' .format(valor_real + ((20 / 100) * valor_real)))
elif pag == '3p':
    print('Haverá um acrescimo de 30 %', end =" ")
    print('Seu total ficou: {}' .format(valor_real + ((30 / 100) * valor_real)))
else:
    print('Forma de pagameto não reconhecida, por favor tente novamente!')
