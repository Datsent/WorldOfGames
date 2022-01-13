import random
def generate_number(difficulty):
    return random.randrange(1, (5 * int(difficulty)) + 1)
def get_guess_from_user(difficulty):
    guess_input = input(f"Please, Enter your guess (1-{5 * int(difficulty)}): ")
    while guess_input.isnumeric() is False or 1 > int(guess_input) or int(guess_input) > (5 * int(difficulty)):
        guess_input = input('Wrong input, try again: ')
    return guess_input
def compare_results(secret_number, guess):
    return  secret_number == int(guess)
def play(difficulty):
    secret_number = generate_number(difficulty)
    guess = get_guess_from_user(difficulty)
    return compare_results(secret_number, guess), secret_number