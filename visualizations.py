@app.route('/visualizations')
def visualizations():
    
    import pandas as pd
    import matplotlib.pyplot as plt

    csv_path = "ESportsGames.csv"

    games_df = pd.read_csv(csv_path, encoding = "utf-8")
    grouped_by_genre_df = games_df.groupby("genre")


    game_groups = grouped_by_genre_df["genre"].count()

    fig, axis = plt.subplots(2, 2, figsize = (35, 40))
    axis[0, 0].bar(list(game_groups.index), list(game_groups.values), color = "blue")
    axis[0, 0].set_xlabel("Genre")
    plt.setp(axis[0, 0].xaxis.get_majorticklabels(), rotation = 90)
    axis[0, 0].set_ylabel("Number of Games")





    player_groups = grouped_by_genre_df["totalplayers"].sum()




    axis[1, 0].bar(list(player_groups.index), list(player_groups.values), color = "red")
    axis[1, 0].set_xlabel("Genre")
    plt.setp(axis[1, 0].xaxis.get_majorticklabels(), rotation = 90)
    axis[1, 0].set_ylabel("Number of Players")



    prize_groups = grouped_by_genre_df["totalearnings"].mean()




    axis[0, 1].bar(list(prize_groups.index), list(prize_groups.values), color = "green")
    axis[0, 1].set_xlabel("Genre")
    plt.setp(axis[0, 1].xaxis.get_majorticklabels(), rotation = 90)
    axis[0, 1].set_ylabel("Average Prize Pool")


    tournament_groups = grouped_by_genre_df["totaltournaments"].sum()




    axis[1, 1].bar(list(tournament_groups.index), list(tournament_groups.values), color = "orange")
    axis[1, 1].set_xlabel("Genre")
    plt.setp(axis[1, 1].xaxis.get_majorticklabels(), rotation = 90)
    axis[1, 1].set_ylabel("Number of Tournaments")

    plt.show()
    plt.tight_layout()
    return render_template('visualizations.html', matplotlibsubplots = "Testing")