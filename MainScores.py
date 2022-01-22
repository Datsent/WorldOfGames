from Utils import *
from Score import add_score
from flask import Flask
from flask import render_template, url_for


#print(score)

app = Flask(__name__)
@app.route('/score')
def score():
    try:
        score = open(SCORES_FILE_NAME, 'r').read()
        return render_template('score.html', SCORE=f'{score}')
    except BaseException:
        error = BAD_RETURN_CODE
        return render_template('error.html', ERROR=error)

if __name__ == '__main__':
    app.run()
