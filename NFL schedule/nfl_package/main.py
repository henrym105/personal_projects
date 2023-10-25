import functionz as f
from objectz import NFLTeam
from objectz import NFLSchedule
import pandas as pd


if __name__ == "__main__":
    
    # create the teams, and put them in a dict for easy access by mascot name
    # teams, teams_dict = f.create_teams()

    # create the league with all of the teams
    # myleague = NFLSchedule(teams)
    myleague = NFLSchedule()

    myleague.set_schedule_outline(debug=False)

    outlines = f.create_schedule_outline_df(myleague)
    print(outlines)
    print("---"*50)

    # print(myleague.teams_dict["Bengals"].schedule)
    myleague.set_real_schedule()
    
