import random
from InquirerPy import prompt

options = ['🍒','🍀','🔔','🥠','🍋']

def game():
    global machine
    machine = random.choices(options, k = 3)
    print(machine)

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


V_points = '🍒'# 5
X_points = '🍀'# 10
XX_points = '🔔'# 20
L_points = '🍋'# 50
C_points = '🥠' # 100

game()

counts = sorted([machine.count(x) for x in set(machine)])

match counts:
    case [3]:
        print('JACKPOT')
        nxt()
    case [1, 2]:     # two of one, one of another
        print('Almost there!')
        nxt()
    case [1, 1, 1]:  # all unique
        print('Better Luck next time!')
        nxt()

# ! TODO: CREATE THE RULES FOR ALL THE OTHER SYMBOLS
