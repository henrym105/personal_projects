from team import NFLTeam
from commissioner import NFLSchedule
import pandas as pd


if __name__ == "__main__":
    # create the league with all of the teams
    league = NFLSchedule()

    league.set_schedule_outline()

    print(league.bengals)
    # print(outline)
    # print("==="*60)
    # print()

    # print(myleague.teams_dict["Bengals"].schedule)
    # myleague.set_real_schedule()
    
