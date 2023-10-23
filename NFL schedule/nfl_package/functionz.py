import random
import objectz as o

def create_teams():
    """ Initialize an object for all 32 NFL Teams

    Returns:
        tuple: (all_teams, AFC, NFC)
    """

    # ----------------------------------------------------------------------------------------------------------------------- #
    # ----------------------------------------------------------------------------------------------------------------------- #
    # def create_new_league():

    # AFC East Teams
    patriots = o.NFLTeam("New England Patriots", "AFC", "East")
    bills = o.NFLTeam("Buffalo Bills", "AFC", "East")
    dolphins = o.NFLTeam("Miami Dolphins", "AFC", "East")
    jets = o.NFLTeam("New York Jets", "AFC", "East")

    # AFC North Teams
    ravens = o.NFLTeam("Baltimore Ravens", "AFC", "North")
    steelers = o.NFLTeam("Pittsburgh Steelers", "AFC", "North")
    browns = o.NFLTeam("Cleveland Browns", "AFC", "North")
    bengals = o.NFLTeam("Cincinnati Bengals", "AFC", "North")

    # AFC South Teams
    texans = o.NFLTeam("Houston Texans", "AFC", "South")
    colts = o.NFLTeam("Indianapolis Colts", "AFC", "South")
    titans = o.NFLTeam("Tennessee Titans", "AFC", "South")
    jaguars = o.NFLTeam("Jacksonville Jaguars", "AFC", "South")

    # AFC West Teams
    chiefs = o.NFLTeam("Kansas City Chiefs", "AFC", "West")
    broncos = o.NFLTeam("Denver Broncos", "AFC", "West")
    raiders = o.NFLTeam("Las Vegas Raiders", "AFC", "West")
    chargers = o.NFLTeam("Los Angeles Chargers", "AFC", "West")

    # NFC East Teams
    cowboys = o.NFLTeam("Dallas Cowboys", "NFC", "East")
    washington = o.NFLTeam("Washington Football Team", "NFC", "East")
    eagles = o.NFLTeam("Philadelphia Eagles", "NFC", "East")
    giants = o.NFLTeam("New York Giants", "NFC", "East")

    # NFC North Teams
    packers = o.NFLTeam("Green Bay Packers", "NFC", "North")
    bears = o.NFLTeam("Chicago Bears", "NFC", "North")
    vikings = o.NFLTeam("Minnesota Vikings", "NFC", "North")
    lions = o.NFLTeam("Detroit Lions", "NFC", "North")

    # NFC South Teams
    buccaneers = o.NFLTeam("Tampa Bay Buccaneers", "NFC", "South")
    saints = o.NFLTeam("New Orleans Saints", "NFC", "South")
    panthers = o.NFLTeam("Carolina Panthers", "NFC", "South")
    falcons = o.NFLTeam("Atlanta Falcons", "NFC", "South")

    # NFC West Teams
    seahawks = o.NFLTeam("Seattle Seahawks", "NFC", "West")
    rams = o.NFLTeam("Los Angeles Rams", "NFC", "West")
    cardinals = o.NFLTeam("Arizona Cardinals", "NFC", "West")
    sf49ers = o.NFLTeam("San Francisco 49ers", "NFC", "West")

    # Create a list of all 32 NFLTeam objects
    nfl_teams = [
        patriots, bills, dolphins, jets,
        ravens, steelers, browns, bengals,
        texans, colts, titans, jaguars,
        chiefs, broncos, raiders, chargers,
        cowboys, washington, eagles, giants,
        packers, bears, vikings, lions,
        buccaneers, saints, panthers, falcons,
        seahawks, rams, cardinals, sf49ers
    ]

    # Create a list of teams in the AFC and NFC
    AFC = [ team for team in nfl_teams if "AFC" in team.conference ]
    NFC = [ team for team in nfl_teams if "NFC" in team.conference ]
    # [team.name for team in AFC]


    for team in nfl_teams:
        team.opponents_not_faced = [team for team in nfl_teams]


    return nfl_teams, AFC, NFC

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


