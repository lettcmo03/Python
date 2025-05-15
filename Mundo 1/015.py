x=int(input('Quantos dias o carro foi alugado? '))
y=float(input('Quantos km o carro rodou? '))
z=float(x*60.00)
a=float(y*0.15)
t=z+a
print('O total a pagar é R$ {:.2f}' .format(t))