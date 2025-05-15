import random
attempt = 0
computer_choice=random.randrange(0, 10)
human_choice=int(input('Pensei eum um número entre 0 e 10, advinhe qual é: '))
while human_choice != computer_choice:
    if human_choice <= 10:
        print('\033[0;31mNão foi desta vez, tente novamente!\033[m')
        attempt += 1
        human_choice = int(input('Tentativa # {}: ' .format(attempt)))
    else:
        print('Numero invalido')
        attempt += 1
        human_choice = int(input('Tentativa # {}: ' .format(attempt)))
print('\033[0;32mParabéns, você acertou!\033[m')
print('Você acertou depois da {}ª tentativa' .format(attempt))
