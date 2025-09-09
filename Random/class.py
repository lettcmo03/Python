# Exercício 3 – Classe com operação simples Crie uma classe chamada Calculadora com dois métodos: somar(a, b) → retorna a soma subtrair(a, b) → retorna a subtração Teste os métodos.
def line():
    print('-'*50)

class Calculadora:
    def somar(self, a, b):
        return a + b
    def subtrair(self, a, b):
        if a < b:
            return b - a
        else:
            return a - b
line()
print('BEM VINDO A CALCULADORA, ESCOLHA A AÇÃO DESEJADA: ')
choice = int(input('[1] - Somar \n[2] - Subtrair\n'))
a = int(input('Digite o 1º numero: '))
b = int(input('Digite o 2º numero: '))
match choice:
    case 1:
        calc = Calculadora()
        res = calc.somar(a, b)
        print(f'O resultado é {res}')
    case 2:
        calc = Calculadora()
        res = calc.subtrair(a, b)
        print(f'O resultado é {res}')