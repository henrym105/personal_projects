import functionz as f
from objectz import NFLTeam
from objectz import NFLSchedule


if __name__ == "__main__":
    # all_teams_list, afc, nfc = f.create_teams()
    # f.assign_bye_weeks(all_teams_list)
    
    teams, teams_dict = f.create_teams()
    myleague = NFLSchedule(teams)
    myleague.set_schedule_outline(debug=False)

    

    
