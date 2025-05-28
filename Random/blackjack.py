import random

def line():
    print('=-'*30)

def set_winner():

    winner = t_player if abs(t_player - 21) < abs(t_house - 21) else t_house
    if winner == t_player:
        print('Since you are closer to 21, you WON!')
    elif winner == t_house:
        print('Since the house is closer to 21, you LOST!')
    elif t_house == t_player:
        print('It is a TIE!')
    
    #asks if the player wants to go again
    start = int(input('Would you like to go again? \n[0] - YES\n[1] - NO\n'))
    if start == 0:
        t_player = 0

line()
print('WELCOME TO BLACKJACK')
line()
#creates a limit for the game
cards = 52
first_run = True

#draw the first two cards for both the house and the player and add them
house = {random.randint(2,11) for x in range(2)}
t_house = sum(house)
player = {random.randrange(2,11) for x in range(2)}
t_player = sum(player)

#inform the player theirs and the house's sum and ask if they want to play
print(f'You are starting with {t_player} and the house started with a {t_house}')
start = int(input('Would you like to: \n[0] - HIT\n[1] - STOP\n'))

first = {first_run, cards != 0, start == 0, t_house < 21, t_player < 21}
more = {first_run, cards != 0, start == 0, t_house < 21, t_player < 21}

# setting the rules for the game
rules = cards != 0 and start == 0 and t_house < 21 and t_player < 21
finish = start == 1, t_player > 21, t_house < 21


#starting the game
while cards != 0 and start == 0 and t_house < 21 and t_player < 21:
    cards -= 1 #each round it takes 1 card
    fist_run = False
    
    #gives the player one more card
    hit = random.randint(1,10) 
    new = hit + t_player
    #that's the new player total, after the hit
    t_player = new 
    
#if both the house and the player are lower than 21    
    if t_player < 21 and t_house < 21: 
            print(f'Your new total is {new}')
            print(f'The house total is {t_house}')
            start = int(input('Would you like to: \n[0] - HIT\n[1] - STOP\n'))

#if the house is lower than 21 but the player is over it    
    elif new > 21 and t_house <= 21:
        print(f'Your total now is {t_player}! Since the house is at {t_house}, You LOST!')
        start = int(input('Would you like to go again? \n[0] - YES\n[1] - NO\n'))
        if start == 0:
            t_player = 0
#if the player is lower than 21 but the house is over it    
    elif t_house > 21 and new <= 21:
        print(f'Your total now is {t_player}! Since the house is at {t_house}, You WON!')
        start = int(input('Would you like to go again? \n[0] - YES\n[1] - NO\n'))        
        if start == 0:
            t_player = 0
#gives the action to see if the player stops before 21
if start == 1:
    rules = False

if t_player < 21: 
    if t_house >= 17:
        print(f'Wise choice, you gave up at {t_player}.')
    
    else:
    #gives the house one more card
        more = random.randint(1,10) 
        table = more + t_house
    
        #that's the new house total, after the hit
        t_house = table 
        print(f'The house chose to buy, it got {t_house}')

#define a winer if the player decides to break first
    winner = t_player if abs(t_player - 21) < abs(t_house - 21) else t_house
    if winner == t_player:
        print('Since you are closer to 21, you WON!')
    elif winner == t_house:
        print('Since the house is closer to 21, you LOST!')
    elif t_house == t_player:
        print('It is a TIE!')
    
    #asks if the player wants to go again
    start = int(input('Would you like to go again? \n[0] - YES\n[1] - NO\n'))
    if start == 0:
        t_player = 0

#continues the game if the player asks to
while {cards != 0, start == 0, t_house < 21, t_player < 21}:
    cards -= 1 #each round it takes 1 card
    fist_run = False
    
    #gives the player one more card
    hit = random.randint(1,10) 
    new = hit + t_player
    #that's the new player total, after the hit
    t_player = new 

    
#if both the house and the player are lower than 21    
    if t_player < 21 and t_house < 21: 
            print(f'Your new total is {new}')
            print(f'The house total is {t_house}')
            start = int(input('Would you like to: \n[0] - HIT\n[1] - STOP\n'))

#if the house is lower than 21 but the player is over it    
    elif new > 21 and t_house <= 21:
        print(f'Your total now is {t_player}! Since the house is at {t_house}, You LOST!')
        start = int(input('Would you like to go again? \n[0] - YES\n[1] - NO\n'))
        if start == 0:
            t_player = 0
#if the player is lower than 21 but the house is over it    
    elif t_house > 21 and new <= 21:
        print(f'Your total now is {t_player}! Since the house is at {t_house}, You WON!')
        start = int(input('Would you like to go again? \n[0] - YES\n[1] - NO\n'))        
        if start == 0:
            t_player = 0
#gives the action to see if the player stops before 21
if start == 1 and t_player < 21: 
    if t_house >= 17:
        print(f'Wise choice, you gave up at {t_player}.')
    
    else:
    #gives the house one more card
        more = random.randint(1,10) 
        table = more + t_house
    
        #that's the new house total, after the hit
        t_house = table 
        print(f'The house chose to buy, it got {t_house}')

#define a winer if the player decides to break first

print('Game Over')
