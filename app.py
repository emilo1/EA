
from flask import Flask, render_template, jsonify
import pandas as pd 

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/tableau')
def tableau():
    return render_template('tableau.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/data')
def data():
    return render_template('data.html')


@app.route('/api/games')
def api_games():
    games_df=pd.read_csv("static/Data/GeneralEsportData.csv")
    games_list= list(games_df["Game"].values)
    games_dictionary={
        "games":games_list
    }
    return jsonify(games_dictionary)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':

    # Run this when running on LOCAL server...
    app.run(debug=True)

    # ...OR run this when PRODUCTION server.
    # app.run(debug=False)