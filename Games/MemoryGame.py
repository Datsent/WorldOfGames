import random
import time, sys
def show_sequence(sequence):
    string_ints = [str(int) for int in sequence]
    str_of_ints = ",".join(string_ints)
    sys.stdout.write('\r' + str_of_ints)
    time.sleep(3)
def hide_sequence():
    print('\r', end='')
def generate_sequence(difficulty):
    '''
    Create random list of numbers. The Length is sum of difficulty with 2
    '''
    sequence_list = []
    for i in range(0, 2 + int(difficulty)):
        n = random.randint(1, 101)
        sequence_list.append(n)
    #show_sequence(sequence_list)
    for i in range(2):
        print(sequence_list, end='\r')
        time.sleep(1)

   # hide_sequence()
    return sequence_list
def get_list_from_user(difficulty):
    guess_string = input(f"Please, enter list of {int(difficulty) + 2} "
                         f"numbers between 1 to 101 (use spaces between numbers): " )
    guess_list = guess_string.split(' ')
    while len(guess_list) != (int(difficulty) + 2) \
            or len([s for s in guess_list if s.isdigit()]) != (int(difficulty) + 2):    # Check correct inputnput
        guess_string = input('Wrong input, try again: ')
        guess_list = guess_string.split(' ')
    return guess_list
def  is_list_equal(sequence, guess):
    for i in range(0, len(guess)):
        guess[i] = int(guess[i])
    return guess == sequence
def play(difficulty):
    sequence = generate_sequence(difficulty)
    guess = get_list_from_user(difficulty)
    return is_list_equal(sequence, guess), sequence


if __name__ == '__main__':
    play("1")