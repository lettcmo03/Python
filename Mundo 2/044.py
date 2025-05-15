import random
start = input('Você está pronto para jogar? ').lower()
if start == 'sim':
    choice = input('Pedra, papel ou tesoura? ').lower()
    bot = random.choice(['pedra', 'papel', 'tesoura'])
    if choice == bot:
        print('Empate')
    elif choice == 'papel' and bot == 'pedra':
        print('Você ganhou! O bot jogou {}' .format(bot))
    elif choice == 'pedra' and bot == 'tesoura':
        print('Você ganhou! O bot jogou {}' .format(bot))
    elif choice == 'tesoura' and bot == 'papel':
        print('Você ganhou! O bot jogou {}' .format(bot))
    elif bot == 'papel' and choice == 'pedra':
        print('Você perdeu! O bot jogou {}' .format(bot))
    elif bot == 'pedra' and choice == 'tesoura':
        print('Você perdeu! O bot jogou {}' .format(bot))
    elif bot == 'tesoura' and choice == 'papel':
        print('Você perdeu! O bot jogou {}' .format(bot))
    else:
        print('Não entendi?')
else:
    print('Obrigada por jogar')