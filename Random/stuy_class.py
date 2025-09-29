from colorama import Fore as f, Style as s
class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0
    def depositar(self):
        deposito = float(input('Quanto gostaria de depositar: R$ '))
        self.saldo += deposito
    def sacar(self):
        saque = float(input('Quanto gostaria de sacar: R$ '))
        self.saldo -= saque
        if self.saldo < 0:
            print(f'{f.RED}Você entrou no negativo! Seu saldo é R$ {self.saldo:.2f}{s.RESET_ALL}')
        else:
            print(f'Saque realizado! Novo saldo: R$ {self.saldo:.2f}')
    def consultar(self):
        print(f'Seu saldo é de R$ {self.saldo:.2f}')
        if self.saldo < 0:
            print(f'{f.RED}Você agora está no negativo!!!, seu saldo é de R$ {self.saldo:.2f}{s.RESET_ALL}')
        elif self.saldo == 0:
            print('Sua conta está zerada!!')

# conta.depositar()
# conta.sacar()
print('BEM VINDO AO APP DO BANCO')
for i in range (1,3):
    titular = input('Para começar, digite o nome do titular da conta: ').title()
    conta = ContaBancaria(titular)
    acao = 0
    while acao!= 4:
        acao = int(input(f'Olá {titular}, gostaria de: \n[1] - sacar \n[2] - consultar \n[3] - depositar \n[4] - sair\n'))
        match acao:
            case 1:
                conta.sacar()
            case 2:
                conta.consultar()
            case 3:
                conta.depositar()
            case 4:
                break
            case _:
                print('Ação inválida')