def linha():
    print('-'*30)

# questão 1
linha()
contribuição = int(input('Quanto tempo trabalhado? '))
idade = int(input('Qual a sua idade? '))
if idade > 65 or contribuição > 35:
    print('Pode se aposentar')
else:
    print('Ainda falta!!!')

# questão 2
linha()
nome = input('Nome do vendedor: ')
salario_real = float(input('Informe o salário base: R$ '))
vendas = float(input('Valor de vendas: R$ '))
comissao = (vendas * (15/100)) + salario_real
print(f'{nome.capitalize()}, seu salario será: R$ {comissao:.2f}')

# questão 3
linha()
print("Tabela de DDDs - Região Sudeste")
linha()
print("11 - São Paulo")
print("19 - Campinas")
print("21 - Rio de Janeiro")
print("22 - Saquarema")
print("27 - Vitória")
print("31 - Belo Horizonte")
linha()

ddd = int(input("Digite o DDD: "))

match ddd:
    case 11:
        print("Cidade: São Paulo")
    case 19:
        print("Cidade: Campinas")
    case 21:
        print("Cidade: Rio de Janeiro")
    case 22:
        print("Cidade: Saquarema")
    case 27:
        print("Cidade: Vitória")
    case 31:
        print("Cidade: Belo Horizonte")
    case _:
        print("DDD não encontrado na região Sudeste")

# questão 4
linha()
num = int(input("Digite um número inteiro: "))
resto = num % 2

match resto:
    case 0:
        print(f"{num} é PAR")
    case 1:
        print(f"{num} é ÍMPAR")