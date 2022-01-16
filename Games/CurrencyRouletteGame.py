from currency_converter import CurrencyConverter
import random
def get_money_interval(difficulty):
    currency = CurrencyConverter()
    random_number = random.randrange(101)
    currency_conver = currency.convert(random_number, 'USD', 'ILS')
    return (round(currency_conver, 2) - (5 - int(difficulty)),
            round(currency_conver, 2) + (5 - int(difficulty)), random_number, currency_conver)
def get_guess_from_user(random_number):
    guess_input = input(f'How much {random_number} USD in ILS? :')
    while guess_input.isnumeric() is False:             # Check correct input
        guess_input = input('Wrong input, try again: ')
    return guess_input
def play (difficulty):
    currency_converter = get_money_interval(difficulty)
    user_guess = int(get_guess_from_user(currency_converter[2]))
    return currency_converter[0] <= user_guess <= currency_converter[1], round(currency_converter[3],2)

if __name__ == '__main__':
    play('1')