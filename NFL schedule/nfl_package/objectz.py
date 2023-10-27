import numpy as np
import copy, json, random, time
import pandas as pd

class NFLTeam():
    def __init__(self, city, mascot, conference, division):
        self.city = city
        self.mascot = mascot
        self.name = city + " " + mascot

        self.conference = conference
        self.division = division
        self.unique_division = f"{self.conference[0]}.{self.division[0]}"

        self.conference_games_played = 0
        self.division_games_played = 0

        self.schedule = {i: None for i in range(1,19)}
        self.schedule_outline = {i: None for i in range(1,19)}
        self.bye_week = None

        self.required_opponents = {"division": None, "conference": None}
        self.opponents_not_faced = []

    def __repr__(self):
        return f"{self.mascot} {self.conference[0]}.{self.division[0]}"

    def __str__(self):
        # return f"{self.name} ({self.conference} {self.division}) - Bye Week: {self.bye_week} - Games Played: {self.games_played}"
        return self.__repr__()
    
    def set_bye_week(self, week_num):
        """assigns week_num (int) as the bye week"""
        self.bye_week = week_num
        self.schedule_outline[week_num] = "-- BYE --"
        self.schedule[self.bye_week] = " -- BYE --"

    def play_game(self, opponent, week_number, home_indicator):
        self.games_played += 1

        if opponent.conference == self.conference:
            self.conference_games_played += 1
            if opponent.division == self.division:
                self.division_games_played += 1

        # delete the opponent from the list of other teams that this team has not played against
        if opponent in self.opponents_not_faced:
            self.opponents_not_faced.remove(opponent)

        # add this game to the team objects schedule
        self.schedule.append({
            'week': week_number,
            'opponent': opponent,
            'home_ind': home_indicator  # You can determine if it's a home game based on your scheduling logic
        })

    def add_game(self, week, opponent):
        self.schedule[int(week)] = opponent


class NFLSchedule():
    """
    Holds the master schedule for the NFL Season, optional parameter weeks set to default = 18
    """
    def __init__(self, weeks = 18):
        # self.allteams = all_NFL_teams
        self.weeks = weeks

        self.allteams = self.create_teams()
        self.teams_dict = {team.mascot: team for team in self.allteams}
        self.AFC = [ team for team in self.allteams if "AFC" in team.conference.upper() ]
        self.NFC = [ team for team in self.allteams if "NFC" in team.conference.upper() ]
        self.teams_played_other_conference = []
        self.schedule = {i: None for i in range(1, weeks+1)}

    def __str__(self):
        # return json.dumps(self.schedule, indent=4)
        return self.allteams

    def create_teams(self) -> list:
        """ Returns a list of the 32 NFLTeam objects, one for each team"""

        # AFC East Teams
        patriots = NFLTeam("New England", "Patriots", "AFC", "East")
        bills = NFLTeam("Buffalo", "Bills", "AFC", "East")
        dolphins = NFLTeam("Miami", "Dolphins", "AFC", "East")
        jets = NFLTeam("New York", "Jets", "AFC", "East")

        # AFC North Teams
        ravens = NFLTeam("Baltimore", "Ravens", "AFC", "North")
        steelers = NFLTeam("Pittsburgh", "Steelers", "AFC", "North")
        browns = NFLTeam("Cleveland", "Browns", "AFC", "North")
        bengals = NFLTeam("Cincinnati", "Bengals", "AFC", "North")

        # AFC South Teams
        texans = NFLTeam("Houston", "Texans", "AFC", "South")
        colts = NFLTeam("Indianapolis", "Colts", "AFC", "South")
        titans = NFLTeam("Tennessee", "Titans", "AFC", "South")
        jaguars = NFLTeam("Jacksonville", "Jaguars", "AFC", "South")

        # AFC West Teams
        chiefs = NFLTeam("Kansas City", "Chiefs", "AFC", "West")
        broncos = NFLTeam("Denver", "Broncos", "AFC", "West")
        raiders = NFLTeam("Las Vegas", "Raiders", "AFC", "West")
        chargers = NFLTeam("Los Angeles", "Chargers", "AFC", "West")

        # NFC East Teams
        cowboys = NFLTeam("Dallas", "Cowboys", "NFC", "East")
        washington = NFLTeam("Washington", "Commanders", "NFC", "East")
        eagles = NFLTeam("Philadelphia", "Eagles", "NFC", "East")
        giants = NFLTeam("New York", "Giants", "NFC", "East")

        # NFC North Teams
        packers = NFLTeam("Green Bay", "Packers", "NFC", "North")
        bears = NFLTeam("Chicago", "Bears", "NFC", "North")
        vikings = NFLTeam("Minnesota", "Vikings", "NFC", "North")
        lions = NFLTeam("Detroit", "Lions", "NFC", "North")

        # NFC South Teams
        buccaneers = NFLTeam("Tampa Bay", "Buccaneers", "NFC", "South")
        saints = NFLTeam("New Orleans", "Saints", "NFC", "South")
        panthers = NFLTeam("Carolina", "Panthers", "NFC", "South")
        falcons = NFLTeam("Atlanta", "Falcons", "NFC", "South")

        # NFC West Teams
        seahawks = NFLTeam("Seattle", "Seahawks", "NFC", "West")
        rams = NFLTeam("Los Angeles", "Rams", "NFC", "West")
        cardinals = NFLTeam("Arizon", "Cardinals", "NFC", "West")
        sf49ers = NFLTeam("San Francisco", "49ers", "NFC", "West")

        # Create a list of all 32 NFLTeam objects
        teams = [patriots, bills, dolphins, jets, ravens, steelers, browns, bengals,
                texans, colts, titans, jaguars,chiefs, broncos, raiders, chargers,
                cowboys, washington, eagles, giants,packers, bears, vikings, lions,
                buccaneers, saints, panthers, falcons, seahawks, rams, cardinals, sf49ers]

        return teams

    def weekly_bye_count(self, eligible_weeks):
        # keep randomly creating the number of teeams on bye for each week until there are 32 bye slots
        weekly_bye_count_list = [random.choice([2,4]) for week in eligible_weeks]
        while sum(weekly_bye_count_list) != 32:
            weekly_bye_count_list =  [random.choice([2,4]) for week in eligible_weeks]

        # add the weeks at start and end of season to fill out the full schedule
        weekly_bye_count_list = [0,0,0] + weekly_bye_count_list + [0,0,0,0]

        # list of how many teams from each conference are on a bye for in each week (index)
        weekly_bye_slots_per_conference = [value//2 for value in weekly_bye_count_list]
        return weekly_bye_slots_per_conference

    def assign_bye_weeks(self, cutoff = 10000, debug = False):
        """ """
        # Byes can only occur from week 4 to week 14 (i.e. range index 3 - 13)
        eligible_weeks = list(range(4, 15)) 
        weekly_bye_slots_per_conference = self.weekly_bye_count(eligible_weeks)
        if debug:
            print(f"{weekly_bye_slots_per_conference = }")

        # Set up a while loop so that if it tries to assign a bye week on a divisional week, it will start over and try again.
        keep_searching = True        
        count = 0
        if debug:
            cutoff = 1
        else:
            cutoff = 10000

        # create temp copies of the self attributes that we need for this round
        AFC_teams = self.AFC.copy()
        NFC_teams = self.NFC.copy()

        # ________________________________________________________________________________________________
        while keep_searching == True:
            random.seed(time.time())

            count += 1
            if debug:
                print(f"{count = }")
            if count > cutoff:
                break

            # create the empty bye list to keep track of who has been assigned a bye week already
            bye_list = {team: None for team in self.allteams}

            # create temp copies of the self attributes that we need for this round
            AFC_teams = self.AFC.copy()
            NFC_teams = self.NFC.copy()
            random.shuffle(AFC_teams)
            random.shuffle(NFC_teams)
            # AFC_teams = list(np.random.shuffle(AFC_teams))
            # NFC_teams = list(np.random.shuffle(NFC_teams))
            if debug:
                print("shuffled teams")

            # for each week when byes can occur, choose "num_slots" teams who are not in divisional play this week for a bye
            for week_num in eligible_weeks:
                if debug:
                    print("_"*50, f"\n{week_num = }")
                for num_slots in range(weekly_bye_slots_per_conference[week_num-1]):
                    # grab 1 or 2 teams from each conference, depending on how many slots are available 
                    eligible_teams_afc = [team for team in AFC_teams if team.schedule_outline[week_num] == None]
                    eligible_teams_nfc = [team for team in NFC_teams if team.schedule_outline[week_num] == None]

                    if debug:
                        print()
                        print(f"{weekly_bye_slots_per_conference[week_num] = }")
                        print(f"{AFC_teams = }")
                        print(f"{NFC_teams = }")
                        print(f"{eligible_teams_afc = }")
                        print(f"{eligible_teams_nfc = }")
                        print()

                    if eligible_teams_afc and eligible_teams_nfc:
                    # if eligible_teams_afc.any() and eligible_teams_nfc.any():
                        """choose AFC team(s)"""
                        # selected_team_a = random.choice(eligible_teams_afc)
                        selected_team_a = eligible_teams_afc[0]
                        
                        # remove that team form the temp list so we don't pick it again
                        AFC_teams.remove(selected_team_a)
                        # replace the default None value with the weeke_number of their bye
                        bye_list[selected_team_a] = week_num

                        """choose NFC team(s)"""
                        # selected_team_n = random.choice(eligible_teams_nfc)
                        selected_team_n = eligible_teams_nfc[0]
                        
                        # remove that team form the temp list so we don't pick it again
                        NFC_teams.remove(selected_team_n)

                        # replace the default None value with the weeke_number of their bye
                        bye_list[selected_team_n] = week_num
                        if debug:
                            print(f"{selected_team_a.name = }")
                            print(f"{selected_team_n.name = }")
                    else:
                        # if there are not any eligible teams from one of the conferences, then break and try again
                        keep_searching = True
                        break
            
            if any(value is None for value in bye_list.values()):
                # At least one team has not been assigned a bye week, so run it back.
                keep_searching = True                
            else:
                # All of the teams have been assigned a bye week, so we have succeeded and do not need to try again.
                print("\nSUCCESS!!")
                if debug:
                    print(f"{count = }")
                    print(f"{bye_list = }")
                keep_searching = False
        
        """ now outside of the while loop """
        print(f"\n{count = }")

        if None in bye_list.values():
            raise Exception(" -- MAX ITERATIONS REACHED -- ")
        elif debug:
            bye_list = dict(sorted(bye_list.items(), key=lambda item: item[1]))
            print(f"{bye_list = }")


        for team, byeweek in bye_list.items():
            team.set_bye_week(byeweek)

        return count, cutoff

    def add_game_to_teams(self, week: int, home_team: NFLTeam, away_team: NFLTeam) -> None:
        """Accesses the pre-defined object for both teams and adds this matchup to the team objects scheduule
        Args:
            week (int): the week that the two teams are playing each other
            home_team (class <NFLTeam>): the home team 
            away_team (class <NFLTeam>): the away team 
        """
        pass

        # if home_team.schedule[week] is None:
        #     self.schedule[week] = {"home": hometeam, "away": awayteam}
        # else:
        #     self.schedule[week] = self.schedule[week] + {"home": hometeam, "away": awayteam}

        # # check if its a divisional or conference game
        # if home_team.conference == home_team.conference:
        #     home_team.conference_games_played += 1
        #     away_team.conference_games_played += 1
        #     # if in conference, check if also in division.
        #     if home_team.division == home_team.division:
        #         home_team.division_games_played += 1
        #         away_team.division_games_played += 1

    def add_game_to_schedule(self, week: int, hometeam: NFLTeam, awayteam: NFLTeam):
        """Adds a pair to the week index of the self.schedule.

        Args:
            week: The week when this game is played.
            hometeam: The home team.
            awayteam: The away team.
        """

        if self.schedule[week] is None:
            self.schedule[week] = []
        self.schedule[week].append([hometeam, awayteam])

    def set_schedule_outline(self, debug = False) -> None:
        """ For each division, set aside 6 weeks for divisional games. add those 6 weeks to each teams sheduule outline
            Then add each team's bye week, continue doing until none of the bye weeks overlap with each teams weeks reserved for divisional games 
        """

        """ 
            !!! ISSUE !!! 
            no more than 2 of the 4 divisons in each conference can have divisional games per week.
        """

        ####################################################################################
        # Establish 6 weeks for each division to play against themselves.
        # currently excluding week 13 and 14 (to ensure we can always have enough teams eligible for a bye week)
        div_eligible_weeks = [1,2,3,4,5,6,7,8,9,10,11,12,13] + [16,17,18]
        unique_divisions = set([team.unique_division for team in self.allteams])

        for div in unique_divisions:
            divisional_game_weeks = sorted(np.random.choice(div_eligible_weeks, size = 6, replace = False))
            for team in [t for t in self.allteams if t.unique_division == div]:
                for week_num in divisional_game_weeks:
                    team.schedule_outline[week_num] = "d"

        print("6 divisional weeks assigned")

        ####################################################################################
        # Set up 1 bye week for all teams:
        x, cutoff = self.assign_bye_weeks(debug)
        if x > cutoff:
            print("FAIL")
        print("1 bye week assigned")

        ####################################################################################
        # Reserve one week for cross-conference games
        open_weeks = list(range(1,19))
        for team in self.allteams:
            for week in open_weeks:
                # if a team has something scheduled that week, remove it from the options
                if team.schedule_outline[week] is not None:
                    open_weeks.remove(week)
        if debug:
            print(f"{open_weeks = }")

        ####################################################################################
        # Reserve the earliest open week for in-conference games
        xconf_week = min(open_weeks)
        for team in self.allteams:
            team.schedule_outline[xconf_week] = "XC"
        print("1 cross-conference week assigned")

        ####################################################################################
        # designate the remaining weeks as random conference games
        for team in self.allteams:
            for week_num in team.schedule_outline.keys():
                if team.schedule_outline[week_num] == None:
                    team.schedule_outline[week_num] = "conf"
        print("remaining weeks set as non-divisional conference games")

        ####################################################################################
        # create the returned dataframe 
        new_dict = {team: team.schedule_outline for team in self.allteams}
        return pd.DataFrame.from_dict(new_dict, orient='index')

    def set_real_schedule(self, debug = False) -> None:
        """each week, find out how which teams are eligble to play each other 

        Args:
            debug (bool, optional): set to True to enable debugging print statements. Defaults to False.
        """

        for week in range(1, 19):
            # need to be sure that every team plays 1 time per week (or has a bye)
            teams_list = self.allteams.copy()
            
            # assign divisional games
            teams_div_game = [team for team in teams_list if team.schedule_outline[week].lower() == "d"]
            unique_divisions = set([team.unique_division for team in teams_div_game])
            for div in unique_divisions:
                div_teams = [team for team in teams_div_game if team.unique_division == div]
                random.shuffle(div_teams)
                while div_teams:
                    home = div_teams.pop()
                    away = div_teams.pop()
                    self.add_game_to_schedule(week = week, hometeam = home, awayteam = away)

            # assign in-conference games
            teams_conf_game = [team for team in teams_list if team.schedule_outline[week] == "conf"]
            conferences = set([team.conference for team in teams_div_game])
            abcdef = 0
            for conf in conferences:
                conf_teams = [team for team in teams_conf_game if team.conference == conf]
                random.shuffle(conf_teams)
                while conf_teams:
                    home = conf_teams.pop()
                    away = conf_teams.pop()
                    self.add_game_to_schedule(week = week, hometeam = home, awayteam = away)

            abcdef = 0
                
            # pass over teams with a bye week
            teams_w_bye = [team for team in teams_list if "bye" in team.schedule_outline[week].lower()]
            
            # assign cross-conference games
            teams_xc_game = [team for team in teams_list if team.schedule_outline[week] == "XC"]
            for team in teams_xc_game:
                pass
            

            # for team in teams_list:
            #     if "bye" in team.schedule_outline[week].lower():
            #         if debug:
            #             print(f"{week = }, bye team = {team.mascot}")

            #         # team.schedule[week] = "-BYE-"
            #         teams_list.remove(team)
            #     if "bye" in team.schedule_outline[week].lower():
            #         pass
            #     if "bye" in team.schedule_outline[week].lower():
            #         pass

            # print(week)
            # self.schedule[week]
