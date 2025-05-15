import random
print('WELCOME TO BLACKJACK')

#creates a limit for the game
cards = 52
first_run = True

#draw the first two cards for both the house and the player and add them
def casa():
    global t_house
    house = {random.randint(2,11) for x in range(2)}
    t_house = sum(house)
    return t_house

def jogador():
    global t_player
    player = {random.randrange(2,11) for x in range(2)}
    t_player = sum(player)
    return t_player

t_player = jogador()
t_house = casa()

#inform the player theirs and the house's sum and ask if they want to play
print(f'You are starting with {t_player} and the house started with a {t_house}')
start = int(input('Would you like to: \n[0] - HIT\n[1] - STOP\n'))

first = {first_run, cards != 0, start == 0, t_house < 21, t_player < 21}
more = {first_run, cards != 0, start == 0, t_house < 21, t_player < 21}


def game():
    #if both the house and the player are lower than 21    
        if t_player < 21 and t_house < 21: 
                print(f'Your new total is {t_player}')
                print(f'The house total is {t_house}')
                start = int(input('Would you like to: \n[0] - HIT\n[1] - STOP\n'))
                return start

    #if the house is lower than 21 but the player is over it    
        elif t_player > 21 and t_house <= 21:
            print(f'Your total now is {t_player}! Since the house is at {t_house}, You LOST!')
            start = int(input('Would you like to go again? \n[0] - YES\n[1] - NO\n'))
            if start == 0:
                t_player = 0
    #if the player is lower than 21 but the house is over it    
        elif t_house > 21 and t_player <= 21:
            print(f'Your total now is {t_player}! Since the house is at {t_house}, You WON!')
            start = int(input('Would you like to go again? \n[0] - YES\n[1] - NO\n'))        
            if start == 0:
                t_player = 0

while (first_run and cards != 0, start == 0, t_house < 21, t_player < 21):
    cards -= 1 #each round it takes 1 card
    fist_run = False
    game()

print('Game Over')
