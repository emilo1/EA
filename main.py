
from flask import Flask, render_template, jsonify
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.stats import linregress 

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


@app.route('/visualizations')
def visualizations():
    twitch = "Twitch_user_data.csv"
    # twitch_df = pd.read_csv(twitch)
    # tw_renamed_df = twitch_df.rename(columns={"Watch time(Minutes)":"Watch", "Stream time(minutes)": "Stream"})
    # # scatter
    # fig,ax = plt.subplots(figsize=(20,10))
    # x_values = tw_renamed_df['Followers']
    # y_values = tw_renamed_df['Followers gained']
    # (slope, intercept, rvalue, pvalue, stderr) = linregress(x_values, y_values)
    # regress_values = x_values * slope + intercept
    # line_eq = "y = " + str(round(slope,2)) + "x + " + str(round(intercept,2))
    # ax.scatter(x_values,y_values)
    # plt.plot(x_values,regress_values,"r-")
    # plt.annotate(line_eq,(0,3000000),fontsize=15,color="red")
    # plt.xlabel('Followers')
    # plt.ylabel('Followers Gained')
    # plt.show()
    # plt.savefig('static/images/scatterplot.png')

    # # stacked bar chart
    # average_peak = tw_renamed_df['Peak viewers'].mean()
    # view_mean = tw_renamed_df['Views gained'].mean()
    # viewer_mean = tw_renamed_df['Average viewers'].mean()

    # period = np.arange(1000, 20000000, 1000)
    # peak = tw_renamed_df.iloc[0:50]['Peak viewers']
    # average = tw_renamed_df.iloc[0:50]['Average viewers']
    # views = tw_renamed_df.iloc[0:50]['Views gained']
    # users = tw_renamed_df.iloc[0:50]['Channel']

    # labels = users.values
    # men_means = peak.values
    # women_means = average.values
    # width = 0.35       # the width of the bars: can also be len(x) sequence

    # fig, ax = plt.subplots(figsize=(20,5))

    # plt.setp(ax.xaxis.get_majorticklabels(), rotation = 90)
    # ax.bar(labels, men_means, width, label='Peak Viewers')
    # ax.bar(labels, women_means, width, bottom=men_means,
    #     label='Average Viewers')

    # ax.set_ylabel('Viewers')
    # ax.set_title('Peak Viewers vs Average Viewers Gained by (50) Twitch Streamers in 2020')
    # ax.legend()

    # plt.show()
    # plt.savefig('static/images/stackedbar.png')
    return render_template('visualizations.html')


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


@app.route('/Trend_lines')
def Trend_lines():
    return render_template('Trend_lines.html')

if __name__ == '__main__':

    # Run this when running on LOCAL server...
    # app.run(debug=True)

    # ...OR run this when PRODUCTION server.
    app.run(debug=False)