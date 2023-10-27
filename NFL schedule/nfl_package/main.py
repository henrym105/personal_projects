import functionz as f
from objectz import NFLTeam
from objectz import NFLSchedule
import pandas as pd


if __name__ == "__main__":
    # create the league with all of the teams
    myleague = NFLSchedule()

    outline = myleague.set_schedule_outline(debug=False)
    print(outline)
    print("==="*60)
    print()

    # print(myleague.teams_dict["Bengals"].schedule)
    # myleague.set_real_schedule()
    
