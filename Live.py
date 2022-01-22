class bcolors:
    '''
    Some colors for outputs
    '''
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
def welcome(name):
    return 'Hello ' + bcolors.BOLD + bcolors.OKGREEN + f'{name}' + bcolors.ENDC + ' and welcome to the World of' \
            ' Games (WoG).\nHere you can find many cool games to play.'

def load_game():
    '''
    The function return user chosen game and the difficulty as list
    '''
    games = ['Memory Game', 'Guess Game', 'Currency Roulette']
    description_game = {
        'Memory Game': 'a sequence of numbers will appear for 1 second and you have to guess it back',
        'Guess Game': 'guess a number and see if you chose like the computer',
        'Currency Roulette': 'try and guess the value of a random amount of USD in ILS'
    }
    for game in games:
       print(f'{(games.index(game) + 1)}. {game} - {description_game[game]}')
    choosen_game = input()
    while choosen_game.isnumeric() is False or int(choosen_game) > len(games) or int(choosen_game) <= 0:
        choosen_game = input('Wrong input, try again: ')
    choosen_difficulty = input("Please choose game difficulty from 1 to 5: ")
    while choosen_difficulty.isnumeric() is False or int(choosen_difficulty) > 5 or int(choosen_difficulty) <= 0:
        choosen_difficulty = input('Wrong input, try again: ')
    return games[int(choosen_game) - 1], choosen_difficulty
