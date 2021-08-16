
from flask import Flask, render_template, jsonify
import matplotlib.pyplot as plt
import pandas as pd

# import datetime
# from scipy import stats
# from scipy.optimize import curve_fit
# from matplotlib.ticker import MaxNLocator
# import matplotlib.pyplot as plt
# from numpy import arange
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error, r2_score

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
    # twitch = "Twitch_user_data.csv"
    # twitch_df = pd.read_csv(twitch)
    # tw_renamed_df = twitch_df.rename(columns={"Watch time(Minutes)":"Watch", "Stream time(minutes)": "Stream"})
    # # scatter
    # fig,ax = plt.subplots(figsize=(15,7))
    # x_values = tw_renamed_df['Followers']
    # y_values = tw_renamed_df['Followers gained']
    # (slope, intercept, rvalue, pvalue, stderr) = linregress(x_values, y_values)
    # regress_values = x_values * slope + intercept
    # line_eq = "y = " + str(round(slope,2)) + "x + " + str(round(intercept,2))
    # ax.scatter(x_values,y_values)
    # ax.plot(x_values,regress_values,"r-")
    # ax.annotate(line_eq,(0,3000000),fontsize=15,color="red")
    # ax.set_xlabel('Followers')
    # ax.set_ylabel('Followers Gained')
    # # plt.show()
    # plt.savefig('static/images/scatterplot.png' , transparent=True)

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

    # fig, ax = plt.subplots(figsize=(15,7))

    # plt.setp(ax.xaxis.get_majorticklabels(), rotation = 90)
    # ax.bar(labels, men_means, width, label='Peak Viewers')
    # ax.bar(labels, women_means, width, bottom=men_means,
    #     label='Average Viewers')

    # ax.set_ylabel('Viewers')
    # ax.set_title('Peak Viewers vs Average Viewers Gained by (50) Twitch Streamers in 2020')
    # ax.legend()

    # plt.show()
    # plt.savefig('static/images/stackedbar.png'  , transparent=True)


    # # Bar Sub Plots
    # csv_path = "https://raw.githubusercontent.com/emilo1/EA/Harrison_Branch/ESportsGames.csv?raw=true"

    # games_df = pd.read_csv(csv_path, encoding = "utf-8")
    # games_df.head()
    # grouped_by_genre_df = games_df.groupby("genre")
    # fig, axis = plt.subplots(2, 2, figsize = (7,13))
    # game_groups = grouped_by_genre_df["genre"].count()


    # axis[0, 0].bar(list(game_groups.index), list(game_groups.values), color = "blue")
    # axis[0, 0].set_xlabel("Genre")
    # plt.setp(axis[0, 0].xaxis.get_majorticklabels(), rotation = 90)
    # axis[0, 0].set_ylabel("Number of Games")

    # player_groups = grouped_by_genre_df["totalplayers"].sum()
    # axis[1, 0].bar(list(player_groups.index), list(player_groups.values), color = "red")
    # axis[1, 0].set_xlabel("Genre")
    # plt.setp(axis[1, 0].xaxis.get_majorticklabels(), rotation = 90)
    # axis[1, 0].set_ylabel("Number of Players")
    # prize_groups = grouped_by_genre_df["totalearnings"].mean()
    # axis[0, 1].bar(list(prize_groups.index), list(prize_groups.values), color = "green")
    # axis[0, 1].set_xlabel("Genre")
    # plt.setp(axis[0, 1].xaxis.get_majorticklabels(), rotation = 90)
    # axis[0, 1].set_ylabel("Average Prize Pool")
    # tournament_groups = grouped_by_genre_df["totaltournaments"].sum()
    # axis[1, 1].bar(list(tournament_groups.index), list(tournament_groups.values), color = "orange")
    # axis[1, 1].set_xlabel("Genre")
    # plt.setp(axis[1, 1].xaxis.get_majorticklabels(), rotation = 90)
    # axis[1, 1].set_ylabel("Number of Tournaments")
    # # plt.show()
    # plt.tight_layout()
    # plt.savefig("static/images/barsubplots.png"  , transparent=True)
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
    # df = pd.read_csv ('static/Data/GeneralEsportData.csv')
    # genre_totals_df= df
    # genre_totals_df[['TotalTournaments']] = genre_totals_df[['TotalTournaments']].astype(float)
    # genre_totals_df= genre_totals_df.drop('OnlineEarnings', 1)
    # genre_totals_df = genre_totals_df[genre_totals_df['TotalEarnings'] > 0.0]
    # genre_totals_df['Result'] = genre_totals_df['TotalEarnings']/genre_totals_df['TotalTournaments']
    
    # Strategy_df=genre_totals_df.loc[genre_totals_df['Genre']=='Strategy']
    # First_Person_Shooter_df=genre_totals_df.loc[genre_totals_df['Genre']=='First-Person Shooter']
    # Multiplayer_Online_Battle_Arena_df=genre_totals_df.loc[genre_totals_df['Genre']=='Multiplayer Online Battle Arena']
    # Role_Playing_Game_df=genre_totals_df.loc[genre_totals_df['Genre']=='Role-Playing Game']
    # Fighting_Game_df=genre_totals_df.loc[genre_totals_df['Genre']=='Fighting Game']
    # Racing_df=genre_totals_df.loc[genre_totals_df['Genre']=='Racing']
    # Sports_df=genre_totals_df.loc[genre_totals_df['Genre']=='Sports']
    # Collectible_Card_Game_df=genre_totals_df.loc[genre_totals_df['Genre']=='Collectible Card Game']
    # Puzzle_Game_df=genre_totals_df.loc[genre_totals_df['Genre']=='Puzzle Game']
    # Battle_Royale_df=genre_totals_df.loc[genre_totals_df['Genre']=='Battle Royale']
    # Third_Person_Shooter_df=genre_totals_df.loc[genre_totals_df['Genre']=='Third-Person Shooter']

    # x=Strategy_df['ReleaseDate']
    # y=Strategy_df['Result']
    # Genre=pd.unique(Strategy_df['Genre'])
    # index = Strategy_df.Game
    # n=len(index) 
    # count=f'Game n={n}'
    # res = stats.linregress(x, y)
    # trend=(f"R-squared: {res.rvalue**2:.6f}")
    # fig1 = plt.figure(figsize=(10,5))
    # plt.plot(x, y, 'o', label=str(count))
    # plt.plot(x, int(res.intercept) + int(res.slope)*x, 'r', label=str(trend))
    # plt.legend()
    # fig1.suptitle(Genre+' Games: Release Year vs. Earnings per Tournament')
    # plt.ylabel('Earnings in USD')
    # plt.xlabel('Year')
    # plt.savefig('static/images/Genre Trends/Strategy1.png')

    # x=First_Person_Shooter_df['ReleaseDate']
    # y=First_Person_Shooter_df['Result']
    # Genre=pd.unique(First_Person_Shooter_df['Genre'])
    # index = First_Person_Shooter_df.Game
    # n=len(index) 
    # count=f'Game n={n}'
    # res = stats.linregress(x, y)
    # trend=(f"R-squared: {res.rvalue**2:.6f}")
    # fig = plt.figure(figsize=(10,5))
    # plt.plot(x, y, 'o', label=str(count))
    # plt.plot(x, int(res.intercept) + int(res.slope)*x, 'r', label=str(trend))
    # plt.legend()
    # fig.suptitle(Genre+' Games: Release Year vs. Earnings per Tournament')
    # plt.xlabel('Year')
    # plt.ylabel('Earnings in USD')
    # plt.savefig('static/images/Genre Trends/First person shooter1.png')
            
    # x=Multiplayer_Online_Battle_Arena_df['ReleaseDate']
    # y=Multiplayer_Online_Battle_Arena_df['Result']
    # Genre=pd.unique(Multiplayer_Online_Battle_Arena_df['Genre'])
    # index = Multiplayer_Online_Battle_Arena_df.Game
    # n=len(index) 
    # count=f'Game n={n}'
    # res = stats.linregress(x, y)
    # trend=(f"R-squared: {res.rvalue**2:.6f}")
    # fig, ax= plt.subplots(figsize=(10,5))
    # ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # plt.plot(x, y, 'o', label=str(count))
    # plt.plot(x, int(res.intercept) + int(res.slope)*x, 'r', label=str(trend))
    # plt.legend()
    # fig.suptitle(Genre+' Games: Release Year vs. Earnings per Tournament')
    # plt.xlabel('Year')
    # plt.ylabel('Earnings in USD')
    # plt.savefig('static/images/Genre Trends/MOBA1.png')

    # x=Role_Playing_Game_df['ReleaseDate']
    # y=Role_Playing_Game_df['Result']
    # Genre=pd.unique(Role_Playing_Game_df['Genre'])
    # index = Role_Playing_Game_df.Game
    # n=len(index) 
    # count=f'Game n={n}'
    # res = stats.linregress(x, y)
    # trend=(f"R-squared: {res.rvalue**2:.6f}")
    # fig = plt.figure(figsize=(10,5))
    # plt.plot(x, y, 'o', label=str(count))
    # plt.plot(x, int(res.intercept) + int(res.slope)*x, 'r', label=str(trend))
    # plt.legend()
    # fig.suptitle(Genre+'s: Release Year vs. Earnings per Tournament')
    # plt.xlabel('Year')
    # plt.ylabel('Earnings in USD')
    # plt.savefig('static/images/Genre Trends/role playing game arena1.png')

            
    # x=Fighting_Game_df['ReleaseDate']
    # y=Fighting_Game_df['Result']
    # Genre=pd.unique(Fighting_Game_df['Genre'])
    # index = Fighting_Game_df.Game
    # n=len(index) 
    # count=f'Game n={n}'
    # res = stats.linregress(x, y)
    # trend=(f"R-squared: {res.rvalue**2:.6f}")
    # fig = plt.figure(figsize=(10,5))
    # plt.plot(x, y, 'o', label=str(count))
    # plt.plot(x, int(res.intercept) + int(res.slope)*x, 'r', label=str(trend))
    # plt.legend()
    # fig.suptitle(Genre+'s: Release Year vs. Earnings per Tournament')
    # plt.xlabel('Year')
    # plt.ylabel('Earnings in USD')
    # plt.savefig('static/images/Genre Trends/fighting games1.png')
            
    # x=Racing_df['ReleaseDate']
    # y=Racing_df['Result']
    # Genre=pd.unique(Racing_df['Genre'])
    # index = Racing_df.Game
    # n=len(index) 
    # count=f'Game n={n}'
    # res = stats.linregress(x, y)
    # trend=(f"R-squared: {res.rvalue**2:.6f}")
    # fig, ax= plt.subplots(figsize=(10,5))
    # ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # plt.plot(x, y, 'o', label=str(count))
    # plt.plot(x, int(res.intercept) + int(res.slope)*x, 'r', label=str(trend))
    # plt.legend()
    # fig.suptitle(Genre+' Games: Release Year vs. Earnings per Tournament')
    # plt.xlabel('Year')
    # plt.ylabel('Earnings in USD')
    # plt.savefig('static/images/Genre Trends/racing game1.png')

    # x=Sports_df['ReleaseDate']
    # y=Sports_df['Result']
    # Genre=pd.unique(Sports_df['Genre'])
    # index = Sports_df.Game
    # n=len(index) 
    # count=f'Game n={n}'
    # res = stats.linregress(x, y)
    # trend=(f"R-squared: {res.rvalue**2:.6f}")
    # fig = plt.figure(figsize=(10,5))
    # plt.plot(x, y, 'o', label=str(count))
    # plt.plot(x, int(res.intercept) + int(res.slope)*x, 'r', label=str(trend))
    # plt.legend()
    # fig.suptitle(Genre+' Games: Release Year vs. Earnings per Tournament')
    # plt.xlabel('Year')
    # plt.ylabel('Earnings in USD')
    # plt.savefig('static/images/Genre Trends/sports1.png')

    # x=Collectible_Card_Game_df['ReleaseDate']
    # y=Collectible_Card_Game_df['Result']
    # Genre=pd.unique(Collectible_Card_Game_df['Genre'])
    # index = Collectible_Card_Game_df.Game
    # n=len(index) 
    # count=f'Game n={n}'
    # res = stats.linregress(x, y)
    # trend=(f"R-squared: {res.rvalue**2:.6f}")
    # fig, ax= plt.subplots(figsize=(10,5))
    # ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # plt.plot(x, y, 'o', label=str(count))
    # plt.plot(x, int(res.intercept) + int(res.slope)*x, 'r', label=str(trend))
    # plt.legend()
    # fig.suptitle(Genre+'s: Release Year vs. Earnings per Tournament')
    # plt.xlabel('Year')
    # plt.ylabel('Earnings in USD')
    # plt.savefig('static/images/Genre Trends/collectible card game1.png')

    # x=Puzzle_Game_df['ReleaseDate']
    # y=Puzzle_Game_df['Result']
    # Genre=pd.unique(Puzzle_Game_df['Genre'])
    # index = Puzzle_Game_df.Game
    # n=len(index) 
    # count=f'Game n={n}'
    # res = stats.linregress(x, y)
    # trend =(f"R-squared: {res.rvalue**2:.6f}")
    # fig = plt.figure(figsize=(10,5))
    # plt.plot(x, y, 'o', label=str(count))
    # plt.plot(x, int(res.intercept) + int(res.slope)*x, 'r', label=str(trend))
    # plt.legend()
    # fig.suptitle(Genre+'s: Release Year vs. Earnings per Tournament')
    # plt.xlabel('Year')
    # plt.ylabel('Earnings in USD')
    # plt.savefig('static/images/Genre Trends/puzzle game1.png')

    # x=Battle_Royale_df['ReleaseDate']
    # y=Battle_Royale_df['Result']
    # Genre=pd.unique(Battle_Royale_df['Genre'])
    # index = Battle_Royale_df.Game
    # n=len(index) 
    # count=f'Game n={n}'
    # res = stats.linregress(x, y)
    # trend=(f"R-squared: {res.rvalue**2:.6f}")
    # fig, ax= plt.subplots(figsize=(10,5))
    # ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # plt.plot(x, y, 'o', label=str(count))
    # plt.plot(x, int(res.intercept) + int(res.slope)*x, 'r', label=str(trend))
    # plt.legend()
    # fig.suptitle(Genre+' Games: Release Year vs. Earnings per Tournament')
    # plt.xlabel('Year')
    # plt.ylabel('Earnings in USD')
    # plt.savefig('static/images/Genre Trends/battle royale1.png')

    # x=Third_Person_Shooter_df['ReleaseDate']
    # y=Third_Person_Shooter_df['Result']
    # Genre=pd.unique(Third_Person_Shooter_df['Genre'])
    # index = Third_Person_Shooter_df.Game
    # n=len(index) 
    # count=f'Game n={n}'
    # res = stats.linregress(x, y)
    # trend=(f"R-squared: {res.rvalue**2:.6f}")
    # fig = plt.figure(figsize=(10,5))
    # plt.plot(x, y, 'o', label=str(count))
    # plt.plot(x, int(res.intercept) + int(res.slope)*x, 'r', label=str(trend))
    # plt.legend()
    # fig.suptitle(Genre+' Games: Release Year vs. Earnings per Tournament')
    # plt.xlabel('Year')
    # plt.ylabel('Earnings in USD')
    # plt.savefig('static/images/Genre Trends/third person shooter1.png')

    # df1 = pd.read_csv ('static/Data/HistoricalEsportData.csv')
    # df1 = df1[df1['Earnings'] > 0.0]
    # df1['Date']= pd.to_datetime(df1['Date'])
    # df1['Date'] = df1['Date'].dt.strftime('%Y')

    # df1[['Date']] = df1[['Date']].astype(float)
    # df1[['Tournaments']] = df1[['Tournaments']].astype(float)

    # df2 = pd.DataFrame()
    # df2["Year"]=pd.unique(df1['Date'])
    # df2["Total"]=list((df1.groupby(["Date"])["Earnings"].sum()))
    # df2["Tournaments"]=list((df1.groupby(["Date"])["Tournaments"].sum()))
    # df2["Avgearnings"]= df2["Total"]/df2["Tournaments"]

    # x = df2.Year.values.reshape(-1, 1)
    # y = df2.Total.values.reshape(-1, 1)
    # y1 = df2.Tournaments.values.reshape(-1, 1)
    # y2 = df2.Avgearnings.values.reshape(-1, 1)

    # model = LinearRegression()
    # model.fit(x, y)
    # x_min = np.array([[x.min()]])
    # x_max = np.array([[x.max()]])
    # y_min = model.predict(x_min)
    # y_max = model.predict(x_max)
    # predicted = model.predict(x)
    # r2 = round(r2_score(y, predicted),2)
    # Trend=f"R-squared (R2 ): {r2}"

    # fig = plt.figure(figsize=(10,5))
    # fig.suptitle('Year vs Total Earnings')
    # plt.xlabel('Year')
    # plt.ylabel('Earnings in USD (by Hundred million)')
    # plt.scatter(x, y, c='blue')
    # plt.plot([x_min[0], x_max[0]], [y_min[0], y_max[0]], c='red',label=str(Trend))
    # plt.legend()
    # plt.savefig('static/images/Historic Trends/Linear Year vs Total Earnings.png')
    
    # model1 = LinearRegression()
    # model1.fit(x, y1)
    # x_min = np.array([[x.min()]])
    # x_max = np.array([[x.max()]])
    # y_min1 = model1.predict(x_min)
    # y_max1 = model1.predict(x_max)
    # predicted = model1.predict(x)
    # r2 = round(r2_score(y1, predicted),2)
    # Trend=f"R-squared (R2 ): {r2}"

    # fig = plt.figure(figsize=(10,5))
    # fig.suptitle('Year vs Tournaments')
    # plt.xlabel('Year')
    # plt.ylabel('Tournaments')
    # plt.scatter(x, y1, c='blue')
    # plt.plot([x_min[0], x_max[0]], [y_min1[0], y_max1[0]], c='red',label=str(Trend))
    # plt.legend()
    # plt.savefig('static/images/Historic Trends/Linear Year vs Total Tournaments.png')

    # model2 = LinearRegression()
    # model2.fit(x, y2)
    # x_min = np.array([[x.min()]])
    # x_max = np.array([[x.max()]])
    # y_min2 = model2.predict(x_min)
    # y_max2 = model2.predict(x_max)
    # predicted = model2.predict(x)
    # r2 = round(r2_score(y2, predicted),2)
    # Trend=f"R-squared (R2 ): {r2}"

    # fig = plt.figure(figsize=(10,5))
    # fig.suptitle('Year vs Earning per Tournament')
    # plt.xlabel('Year')
    # plt.ylabel('Earnings in USD')
    # plt.scatter(x, y2, c='blue')
    # plt.plot([x_min[0], x_max[0]], [y_min2[0], y_max2[0]], c='red',label=str(Trend))
    # plt.legend()
    # plt.savefig('static/images/Historic Trends/Linear Year vs Earning per Tournament.png')

    # def objective(x, a, b, c):
    #     return a * x + b * x**2 + c
    

    # x, y = df2['Year'], df2['Total']

    # popt, _ = curve_fit(objective, x, y)

    # a, b, c = popt

    # x_line = arange(min(x), max(x), 1)

    # y_line = objective(x_line, a, b, c)

    # residuals = y- objective(x, *popt)
    # ss_res = np.sum(residuals**2)
    # ss_tot = np.sum((y-np.mean(y))**2)
    # r_squared =round(1 - (ss_res / ss_tot),2)
    # Trend=f"R-squared: {r_squared}"

    # fig = plt.figure(figsize=(10,5))
    # plt.scatter(x, y)
    # fig.suptitle('Year vs Total Earnings')
    # plt.xlabel('Year')
    # plt.ylabel('Earnings in USD')

    # plt.plot(x_line, y_line, '--', color='red',label=str(Trend))
    # plt.legend()
    # plt.savefig('static/images/Historic Trends/polynomial Year vs Total Earnings.png')

    # def objective(x, a, b, c):
    #     return a * x + b * x**2 + c
    
    # x, y = df2['Year'], df2['Tournaments']

    # popt, _ = curve_fit(objective, x, y)

    # a, b, c = popt
    # x_line = arange(min(x), max(x), 1)
    # y_line = objective(x_line, a, b, c)

    # residuals = y- objective(x, *popt)
    # ss_res = np.sum(residuals**2)
    # ss_tot = np.sum((y-np.mean(y))**2)
    # r_squared =round(1 - (ss_res / ss_tot),2)
    # Trend=f"R-squared: {r_squared}"

    # fig = plt.figure(figsize=(10,5))
    # plt.scatter(x, y)
    # fig.suptitle('Year vs Tournaments')
    # plt.xlabel('Year')
    # plt.ylabel('Tournaments')

    # plt.plot(x_line, y_line, '--', color='red',label=str(Trend))
    # plt.legend()
    # plt.savefig('static/images/Historic Trends/polynomial Year vs Tournament.png')

    # def objective(x, a, b, c):
    #     return a * x + b * x**2 + c
    
    # x, y = df2['Year'], df2['Avgearnings']

    # popt, _ = curve_fit(objective, x, y)

    # a, b, c = popt

    # x_line = arange(min(x), max(x), 1)
    # y_line = objective(x_line, a, b, c)

    # residuals = y- objective(x, *popt)
    # ss_res = np.sum(residuals**2)
    # ss_tot = np.sum((y-np.mean(y))**2)
    # r_squared =round(1 - (ss_res / ss_tot),2)
    # Trend=f"R-squared: {r_squared}"

    # fig = plt.figure(figsize=(10,5))
    # plt.scatter(x, y)
    # fig.suptitle('Year vs Earnings per Tournaments')
    # plt.xlabel('Year')
    # plt.ylabel('Earnings in USD')

    # plt.plot(x_line, y_line, '--', color='red',label=str(Trend))
    # plt.legend()
    # plt.savefig('static/images/Historic Trends/polynomial Year vs Earning per Tournament.png')
    return render_template('Trend_lines.html')

if __name__ == '__main__':

    # Run this when running on LOCAL server...
    # app.run(debug=True)

    # ...OR run this when PRODUCTION server.
    app.run(debug=False)