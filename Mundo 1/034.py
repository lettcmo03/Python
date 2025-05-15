s=float(input('Salário atual: R$ '))
if s<=1250.00:
    a=float(s*(15/100))
    t=s+a
    print('Parabéns, você passará a receber R$ {:.2f}!' .format(t))
else:
    a=float(s*(10/100))
    t=s+a
    print('Parabéns, você passará a receber R$ {:.2f}!' .format(t))