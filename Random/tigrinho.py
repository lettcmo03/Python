import random

options = ['🍒','🍀','🔔','🥠','🍋']

def game():
    global machine
    machine = random.choices(options, k = 3)
    print(machine)

V_points = '🍒'# 5
X_points = '🍀'# 10
XX_points = '🔔'# 20
L_points = '🍋'# 50
C_points = '🥠' # 100

game()

counts = sorted([machine.count(x) for x in set(machine)])

match counts:
    case [3]:
        print('JACKPOT\nWanna play again?')
    case [1, 2]:     # two of one, one of another
        print('Almost there!\nWanna play again?')
    case [1, 1, 1]:  # all unique
        print('Better Luck next time!\nWanna play again?')

# ! TODO: CREATE THE RULES FOR ALL THE OTHER SYMBOLS

play = input('Would you like to go again?[ENTER / Q]: ').lstrip().upper()
if play.isspace == True:
    print('here we go again')
