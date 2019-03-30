from flask import Flask, render_template, url_for
from modules import convert_to_dict

from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret key goes here'
#change this

Bootstrap(app)

games_list = convert_to_dict("newGames.csv")

@app.route("/")
def index():
    ids_list = []
    name_list = []

    for games in games_list:
        ids_list.append(games['id'])
        name_list.append(games['game'])
    pairs_list = zip(ids_list, name_list)
    return render_template('index.html', pairs=pairs_list, the_title ="Games Index")



@app.route('/games/<num>')
def detail(num):
    for games in games_list:
        if games['id'] == num:
            game_dict = games
            break
    # a little bonus function, imported
    return render_template('theGames.html', gamesDict=game_dict, the_title=game_dict['game'])




if __name__ == '__main__':
    app.run(debug=True)
