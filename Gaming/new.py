from InquirerPy import prompt

def nxt(counts=None):
    play = [
        {
            'type': 'list',
            'name': 'again',
            'message': 'Would you like to go again?',
            'choices': ['Yes', 'No']
        }
    ]

    answer = prompt(play)
    if not answer or 'again' not in answer:
        print("No answer received. Stopping.")
        return False

    if answer['again'].strip().lower() == 'no':
        print('Stopping Now!')
        return False
    else:
        print('Here we go again!\n')
        return True
