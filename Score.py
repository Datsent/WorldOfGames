from os import path
from Utils import *
def add_score(difficulty):
    '''
    The function add score to txt file or create new score file.
    '''
    points_of_winning = (int(difficulty) * 3) + 5
    score_file = open(SCORES_FILE_NAME, 'r')
    points_of_winning = int(score_file.read()) + (int(difficulty) * 3) + 5
    score_file.close()
    score_file = open(SCORES_FILE_NAME, 'w')
    score_file.write(str(points_of_winning))
    score_file.close()

if __name__ == '__main__':
    add_score('3')
