import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import pprint
import datetime
from scipy import stats
from scipy.optimize import curve_fit

df = pd.read_csv ('Resources/GeneralEsportData.csv')
genre_totals_df= df
genre_totals_df[['TotalTournaments']] = genre_totals_df[['TotalTournaments']].astype(float)
genre_totals_df= genre_totals_df.drop('OnlineEarnings', 1)
genre_totals_df = genre_totals_df[genre_totals_df['TotalEarnings'] > 0.0]
#genre_totals_df[['ReleaseDate']] = genre_totals_df[['ReleaseDate']].astype(int)
genre_totals_df['Result'] = genre_totals_df['TotalEarnings']/genre_totals_df['TotalTournaments']
        #seperate dataframes by genre
Strategy_df=genre_totals_df.loc[genre_totals_df['Genre']=='Strategy']

First_Person_Shooter_df=genre_totals_df.loc[genre_totals_df['Genre']=='First-Person Shooter']

Multiplayer_Online_Battle_Arena_df=genre_totals_df.loc[genre_totals_df['Genre']=='Multiplayer Online Battle Arena']

Role_Playing_Game_df=genre_totals_df.loc[genre_totals_df['Genre']=='Role-Playing Game']

Fighting_Game_df=genre_totals_df.loc[genre_totals_df['Genre']=='Fighting Game']

Racing_df=genre_totals_df.loc[genre_totals_df['Genre']=='Racing']

Sports_df=genre_totals_df.loc[genre_totals_df['Genre']=='Sports']

Collectible_Card_Game_df=genre_totals_df.loc[genre_totals_df['Genre']=='Collectible Card Game']

Puzzle_Game_df=genre_totals_df.loc[genre_totals_df['Genre']=='Puzzle Game']

Battle_Royale_df=genre_totals_df.loc[genre_totals_df['Genre']=='Battle Royale']

Third_Person_Shooter_df=genre_totals_df.loc[genre_totals_df['Genre']=='Third-Person Shooter']
        #Strategy
x=Strategy_df['ReleaseDate']
y=Strategy_df['Result']
Genre=pd.unique(Strategy_df['Genre'])
res = stats.linregress(x, y)
trend=(f"R-squared: {res.rvalue**2:.6f}")
fig1 = plt.figure(figsize=(10,5))
plt.plot(x, y, 'o', label='Game')
plt.plot(x, int(res.intercept) + int(res.slope)*x, 'r', label=str(trend))
plt.legend()
fig1.suptitle(Genre+' Games: Release Year vs. Earnings per Tournament')
plt.ylabel('Earnings in USD')
plt.xlabel('Year')
plt.savefig('Images/Strategy.png')
plt.show()


        #First person shooter
x=First_Person_Shooter_df['ReleaseDate']
y=First_Person_Shooter_df['Result']
Genre=pd.unique(First_Person_Shooter_df['Genre'])
res = stats.linregress(x, y)
trend=(f"R-squared: {res.rvalue**2:.6f}")
fig = plt.figure(figsize=(10,5))
plt.plot(x, y, 'o', label='Game')
plt.plot(x, int(res.intercept) + int(res.slope)*x, 'r', label=str(trend))
plt.legend()
fig.suptitle(Genre+' Games: Release Year vs. Earnings per Tournament')
plt.xlabel('Year')
plt.ylabel('Earnings in USD')
plt.savefig('Images/First person shooter.png')
plt.show()
        #Multiplayer online battle arena  
        #X ticks are messed up
x=Multiplayer_Online_Battle_Arena_df['ReleaseDate']
y=Multiplayer_Online_Battle_Arena_df['Result']
Genre=pd.unique(Multiplayer_Online_Battle_Arena_df['Genre'])
res = stats.linregress(x, y)
trend=(f"R-squared: {res.rvalue**2:.6f}")
fig = plt.figure(figsize=(10,5))
plt.plot(x, y, 'o', label='Game')
plt.plot(x, int(res.intercept) + int(res.slope)*x, 'r', label=str(trend))
plt.legend()
fig.suptitle(Genre+' Games: Release Year vs. Earnings per Tournament')
plt.xlabel('Year')
plt.ylabel('Earnings in USD')
plt.savefig('Images/MOBA.png')
plt.show()
        #role playing game
x=Role_Playing_Game_df['ReleaseDate']
y=Role_Playing_Game_df['Result']
Genre=pd.unique(Role_Playing_Game_df['Genre'])
res = stats.linregress(x, y)
trend=(f"R-squared: {res.rvalue**2:.6f}")
fig = plt.figure(figsize=(10,5))
plt.plot(x, y, 'o', label='Game')
plt.plot(x, int(res.intercept) + int(res.slope)*x, 'r', label=str(trend))
plt.legend()
fig.suptitle(Genre+'s: Release Year vs. Earnings per Tournament')
plt.xlabel('Year')
plt.ylabel('Earnings in USD')
plt.savefig('Images/role playing game arena.png')
plt.show()
        #fighting games
x=Fighting_Game_df['ReleaseDate']
y=Fighting_Game_df['Result']
Genre=pd.unique(Fighting_Game_df['Genre'])
res = stats.linregress(x, y)
trend=(f"R-squared: {res.rvalue**2:.6f}")
fig = plt.figure(figsize=(10,5))
plt.plot(x, y, 'o', label='Game')
plt.plot(x, int(res.intercept) + int(res.slope)*x, 'r', label=str(trend))
plt.legend()
fig.suptitle(Genre+'s: Release Year vs. Earnings per Tournament')
plt.xlabel('Year')
plt.ylabel('Earnings in USD')
plt.savefig('Images/fighting games.png')
plt.show()

        #racing game
        #X ticks are messed up
x=Racing_df['ReleaseDate']
y=Racing_df['Result']
Genre=pd.unique(Racing_df['Genre'])
res = stats.linregress(x, y)
trend=(f"R-squared: {res.rvalue**2:.6f}")
fig = plt.figure(figsize=(10,5))
plt.plot(x, y, 'o', label='Game')
plt.plot(x, int(res.intercept) + int(res.slope)*x, 'r', label=str(trend))
plt.legend()
fig.suptitle(Genre+' Games: Release Year vs. Earnings per Tournament')
plt.xlabel('Year')
plt.ylabel('Earnings in USD')
plt.savefig('Images/racing game.png')
plt.show()
        #sports
x=Sports_df['ReleaseDate']
y=Sports_df['Result']
Genre=pd.unique(Sports_df['Genre'])
res = stats.linregress(x, y)
trend=(f"R-squared: {res.rvalue**2:.6f}")
fig = plt.figure(figsize=(10,5))
plt.plot(x, y, 'o', label='Game')
plt.plot(x, int(res.intercept) + int(res.slope)*x, 'r', label=str(trend))
plt.legend()
fig.suptitle(Genre+' Games: Release Year vs. Earnings per Tournament')
plt.xlabel('Year')
plt.ylabel('Earnings in USD')
plt.savefig('Images/sports.png')
plt.show()
        #collectible card game
        #X ticks are messed up
x=Collectible_Card_Game_df['ReleaseDate']
y=Collectible_Card_Game_df['Result']
Genre=pd.unique(Collectible_Card_Game_df['Genre'])
res = stats.linregress(x, y)
trend=(f"R-squared: {res.rvalue**2:.6f}")
fig = plt.figure(figsize=(10,5))
plt.plot(x, y, 'o', label='Game')
plt.plot(x, int(res.intercept) + int(res.slope)*x, 'r', label=str(trend))
plt.legend()
fig.suptitle(Genre+'s: Release Year vs. Earnings per Tournament')
plt.xlabel('Year')
plt.ylabel('Earnings in USD')
plt.savefig('Images/collectible card game.png')
plt.show()
        #puzzle game
x=Puzzle_Game_df['ReleaseDate']
y=Puzzle_Game_df['Result']
Genre=pd.unique(Puzzle_Game_df['Genre'])
res = stats.linregress(x, y)
trend =(f"R-squared: {res.rvalue**2:.6f}")
fig = plt.figure(figsize=(10,5))
plt.plot(x, y, 'o', label='Game')
plt.plot(x, int(res.intercept) + int(res.slope)*x, 'r', label=str(trend))
plt.legend()
fig.suptitle(Genre+'s: Release Year vs. Earnings per Tournament')
plt.xlabel('Year')
plt.ylabel('Earnings in USD')
plt.savefig('Images/puzzle game.png')
plt.show()
        #battle royale
        #X ticks are messed up
x=Battle_Royale_df['ReleaseDate']
y=Battle_Royale_df['Result']
Genre=pd.unique(Battle_Royale_df['Genre'])
res = stats.linregress(x, y)
trend=(f"R-squared: {res.rvalue**2:.6f}")
fig = plt.figure(figsize=(10,5))
plt.plot(x, y, 'o', label='Game')
plt.plot(x, int(res.intercept) + int(res.slope)*x, 'r', label=str(trend))
plt.legend()
fig.suptitle(Genre+' Games: Release Year vs. Earnings per Tournament')
plt.xlabel('Year')
plt.ylabel('Earnings in USD')
plt.savefig('Images/battle royale.png')
plt.show()
        #third person shooter
x=Third_Person_Shooter_df['ReleaseDate']
y=Third_Person_Shooter_df['Result']
Genre=pd.unique(Third_Person_Shooter_df['Genre'])
res = stats.linregress(x, y)
trend=(f"R-squared: {res.rvalue**2:.6f}")
fig = plt.figure(figsize=(10,5))
plt.plot(x, y, 'o', label='Game')
plt.plot(x, int(res.intercept) + int(res.slope)*x, 'r', label=str(trend))
plt.legend()
fig.suptitle(Genre+' Games: Release Year vs. Earnings per Tournament')
plt.xlabel('Year')
plt.ylabel('Earnings in USD')
plt.savefig('Images/third person shooter.png')
plt.show()