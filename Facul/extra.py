valor = 0.0
def descontos():
    global valor
    perfil = int(input('Tipo de desconto: \n[1] - Estudante \n[2] - Idoso \n[3] - Fidelidade\n'))
    match perfil:
        case 1:
            valor -= (valor * (10/100))
        case 2:
            valor -= (valor * (15/100))
        case 3:
            valor -= (valor * (5/100))
        case _:
            pass
    return valor
def pagamento():
    global valor
    pag = int(input('Forma de pagamento: \n[1] - Cartão \n[2] - Dinheiro \n[3] - Pix\n'))
    match pag:
        case 1:
            valor
        case 2:
            valor -= (valor * (3/100))
        case 3:
            valor -= (valor * (5/100))
        case _:
            print('Invalido')
    return valor
def antecedencia():
    global valor
    days = int(input('Estamos a quanto tempo da viagem? '))
    if days >= 60:
        valor -= (valor * (8/100))
    elif 30 <= days <= 59:
        valor -= (valor * (5/100))
    else:
        pass
    return valor
def cupom():
    global valor
    ticket = input('Possui cupom de desconto: ').upper()
    if ticket == 'PROMO10':
        valor -= (valor * (10/100))
    elif ticket == 'PROMO5':
        valor -= (valor * (5/100))
    else:
        pass
    return valor
def destino():
    global valor
    destination = int(input('Para onde você vai? \n[1] - Rio de Janeiro \n[2] - São Paulo \n[3] - Salvador\n'))
    match destination:
        case 1:
            valor = 500.0
            descontos()
            pagamento()
            antecedencia()
            cupom()
        case 2:
            valor = 450.0
            descontos()
            pagamento()
            antecedencia()
            cupom()
        case 3:
            valor = 600.0
            descontos()
            pagamento()
            antecedencia()
            cupom()
        case _:
            print('Opção Inválida')
    return valor
destino()
print(f'Total R$ {valor:.2f}')