from os import path
def add_score(difficulty):
    '''
    The function add score to txt file or create new score file.
    '''
    points_of_winning = (int(difficulty) * 3) + 5
    if path.exists('score.txt'):
        score_file = open('score.txt', 'r')
        points_of_winning = int(score_file.read()) + (int(difficulty) * 3) + 5
        score_file.close()
        score_file = open('score.txt', 'w')
        score_file.write(str(points_of_winning))
        score_file.close()
    else:
        score_file = open('score.txt', 'w')
        score_file.write(str(points_of_winning))
        score_file.close()
if __name__ == '__main__':
    add_score('3')
