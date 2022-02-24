from Live import load_game, welcome
from Games import GuessGame, MemoryGame, CurrencyRouletteGame
from Score import add_score
from Utils.Utils import *
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
def results(user_choose):
    if user_choose[0] == "Guess Game":
        result = GuessGame.play(user_choose[1])
        if result[0]:
            print("You are " + bcolors.BOLD + bcolors.OKGREEN + "WINNER" + bcolors.ENDC)
            add_score(user_choose[1])
        else:
            print(bcolors.FAIL + ":( LOOSER ):" + bcolors.ENDC)
            print(f"The number is {result[1]}")
    elif user_choose[0] == "Memory Game":
        result = MemoryGame.play(user_choose[1])
        if result[0]:
            print("You are " + bcolors.BOLD + bcolors.OKGREEN + "WINNER" + bcolors.ENDC)
            add_score(user_choose[1])
        else:
            print(bcolors.FAIL + ":( LOOSER ):" + bcolors.ENDC)
            print(f"The number is {result[1]}")
    elif user_choose[0] == "Currency Roulette":
        result = CurrencyRouletteGame.play(user_choose[1])
        print(result)
        if result[0]:
            print(f"The result is {result[1]} You are " + bcolors.BOLD + bcolors.OKGREEN
                  + "WINNER" + bcolors.ENDC)
            add_score(user_choose[1])
        else:
            print(bcolors.FAIL + ":( LOOSER ):" + bcolors.ENDC)
            print(f"The number is {result[1]}")
def main():
    clear_screen()
    print(welcome(input('Please, enter your name: ')))
    user_choose = load_game()
    score_file = open(SCORES_FILE_NAME, 'w')
    score_file.write('0')
    score_file.close()
    print('Chosen Game is:', user_choose[0], '\nChosen Difficult is:', user_choose[1])
    results(user_choose)
    ask_for_continue = ""
    while ask_for_continue != '3':
        ask_for_continue = input('You want:\n1. Play again this game.\n2. Choose another Game.\n3. Exit.')
        while ask_for_continue.isnumeric() is False or int(ask_for_continue) > 3 or int(ask_for_continue) <= 0:
            ask_for_continue = input('Wrong input, try again: ')  # Check correct input
        if ask_for_continue == '1':
            clear_screen()
            results(user_choose)
        elif ask_for_continue == '2':
            clear_screen()
            user_choose = load_game()
            results(user_choose)
        else:
            print("Thank you, Goodbay <3 !!!")

if __name__ == '__main__':
    main()