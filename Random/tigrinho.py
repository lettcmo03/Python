import random
from InquirerPy import prompt
import sys
import time
from colorama import Fore as f, Style

options = ['🍒','🍀','🔔','🥠','🍋']

def spin(reels=3, spins=15):
    global machine
    for i in range(spins):
        machine = [random.choice(options) for _ in range(reels)]
        sys.stdout.write("\r" + " | ".join(machine))
        sys.stdout.flush()
        time.sleep(0.1 + i * 0.02)  # gradually slow down
    print()  # move to next line

def nxt():
    play = [
        {
            'type': 'list',
            'name': 'again',
            'message': 'Would you like to go again? ',
            'choices': ['Yes', 'No']
        }
    ]

    while True:
        answer = prompt(play)
        if not answer or 'again' not in answer:
            print("No answer received. Stopping.")
            break

        # Compare ignoring case/spacing
        if answer['again'].strip().lower() == 'no':
            print('Stopping Now!')
            break
        else:
            print('Here we go again!')
            game()

def checking_results():
    counts = sorted([machine.count(x) for x in set(machine)])

    match counts:
        case [3]:
            print(f.GREEN + 'JACKPOT!' + Style.RESET_ALL)
        case [1, 2]:
            print(f.YELLOW + 'Almost there!' + Style.RESET_ALL)
        case [1, 1, 1]:
            print(f.LIGHTRED_EX + 'Better luck next time!' + Style.RESET_ALL)
V_points = '🍒'# 5
X_points = '🍀'# 10
XX_points = '🔔'# 20
L_points = '🍋'# 50
C_points = '🥠' # 100

def game():
    spin()
    checking_results()
    nxt()

game()