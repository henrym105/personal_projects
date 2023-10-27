import random
import pandas as pd
from objectz import NFLSchedule


def add_game_to_team(home_team, away_team):
    """ Accesses the pre-defined object for both teams and adds this matchup to the team 
        objects scheduule
    Args:
        home_team (class <NFLTeam>): the NFLTeam object that represents the home team for this game
        away_team (class <NFLTeam>): the NFLTeam object that represents the away team for this game
    """
    # check if its a divisional or conference game
    if home_team.conference == home_team.conference:
        home_team.conference_games_played += 1
        away_team.conference_games_played += 1
        # if in conference, check if in division. can only be in division if also in conference
        if home_team.division == home_team.division:
            home_team.division_games_played += 1
            away_team.division_games_played += 1
    # home_team.s

def assign_bye_weeks(list_of_teams):    
    """Creates the bye weeks and assign each team's .bye_week attribute
        Bye Week Rules:
            - byes occur from week 4 through weeek 14
            - 2 or 4 teams have byes in any given week
            - must be same number of teams from the AFC and NFC on bye each week
            - each team has exactly 1 bye week per season
    Args:
        list_of_teams (list): a list of NFLTeam objects that represent all 32 teams in the NFL
    Returns:
        dict: a dictionary with key = week_num (int) and value = [team.name, team.conference] for
              each team with a bye that week 
        *** NOTE: the returned dict is just a visual aid ***
    """

    eligible_weeks = list(range(4, 15))

    # keep randomly creating the number of teeams on bye for each week until there are 32 bye slots
    weekly_bye_count_list = [random.choice([2,4]) for week in eligible_weeks]
    while sum(weekly_bye_count_list) != 32:
        weekly_bye_count_list =  [random.choice([2,4]) for week in eligible_weeks]

    weekly_bye_count_list = [0,0,0] + weekly_bye_count_list + [0,0,0,0]
    weekly_bye_slots_per_conference = [value//2 for value in weekly_bye_count_list]
    # print(weekly_bye_count_list, weekly_bye_slots_per_conference)

    # create a copy of the nflteams list so the .pop() method doesn't destroy the list
    all_teams_copy = list_of_teams.copy()
    # shuffle the teams to randomize when each team gets the bye week
    random.shuffle(all_teams_copy)


    # afccopy = AFC.copy()
    # nfccopy = NFC.copy()
    afc_teams = [ team for team in all_teams_copy if "AFC" in team.conference ]
    nfc_teams = [ team for team in all_teams_copy if "NFC" in team.conference ]
    # shuffle the conferences to randomize when each team gets the bye week
    random.shuffle(afc_teams)
    random.shuffle(nfc_teams)

    for week_num in range(len(weekly_bye_count_list)):
        # adjusting 0 index lists in python to fit real world terms
        real_week_num = week_num + 1

        for num_slots in range(weekly_bye_slots_per_conference[week_num]):
            # pop 1 team from the AFC and 1 from the NFC
            afcteam = afc_teams.pop()
            nfcteam = nfc_teams.pop()

            afcteam.set_bye_week(real_week_num)
            nfcteam.set_bye_week(real_week_num)
            # print("\t", afcteam.name, afcteam.bye_week, "--", nfcteam.name, nfcteam.bye_week)

    print({week: [[team.name, team.conference] for team in list_of_teams if team.bye_week == week] for week in eligible_weeks})
    # return bye_week_summary

def create_schedule_outline_df(league: NFLSchedule) -> pd.DataFrame:
    new_dict = {team: team.schedule_outline for team in league.allteams}
    return pd.DataFrame.from_dict(new_dict, orient='index')