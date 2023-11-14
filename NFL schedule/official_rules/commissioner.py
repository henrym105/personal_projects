from team import NFLTeam, Conference, Division, Game
import numpy as np
import copy, json, random, time
import pandas as pd


class NFLSchedule():
    """ Holds the master schedule for the NFL Season """
    def __init__(self):
        self.schedule = {f"week_{i}": None for i in range(1, 19)}

        # AFC North Teams
        self.bengals = NFLTeam("Cincinnati", "Bengals", "AFC", "North")
        self.ravens = NFLTeam("Baltimore", "Ravens", "AFC", "North")
        self.steelers = NFLTeam("Pittsburgh", "Steelers", "AFC", "North")
        self.browns = NFLTeam("Cleveland", "Browns", "AFC", "North")

        # AFC South Teams
        self.texans = NFLTeam("Houston", "Texans", "AFC", "South")
        self.colts = NFLTeam("Indianapolis", "Colts", "AFC", "South")
        self.titans = NFLTeam("Tennessee", "Titans", "AFC", "South")
        self.jaguars = NFLTeam("Jacksonville", "Jaguars", "AFC", "South")

        # AFC East Teams
        self.patriots = NFLTeam("New England", "Patriots", "AFC", "East")
        self.bills = NFLTeam("Buffalo", "Bills", "AFC", "East")
        self.dolphins = NFLTeam("Miami", "Dolphins", "AFC", "East")
        self.jets = NFLTeam("New York", "Jets", "AFC", "East")

        # AFC West Teams
        self.chiefs = NFLTeam("Kansas City", "Chiefs", "AFC", "West")
        self.broncos = NFLTeam("Denver", "Broncos", "AFC", "West")
        self.raiders = NFLTeam("Las Vegas", "Raiders", "AFC", "West")
        self.chargers = NFLTeam("Los Angeles", "Chargers", "AFC", "West")

        # NFC North Teams
        self.packers = NFLTeam("Green Bay", "Packers", "NFC", "North")
        self.bears = NFLTeam("Chicago", "Bears", "NFC", "North")
        self.vikings = NFLTeam("Minnesota", "Vikings", "NFC", "North")
        self.lions = NFLTeam("Detroit", "Lions", "NFC", "North")

        # NFC South Teams
        self.buccaneers = NFLTeam("Tampa Bay", "Buccaneers", "NFC", "South")
        self.saints = NFLTeam("New Orleans", "Saints", "NFC", "South")
        self.panthers = NFLTeam("Carolina", "Panthers", "NFC", "South")
        self.falcons = NFLTeam("Atlanta", "Falcons", "NFC", "South")

        # NFC East Teams
        self.cowboys = NFLTeam("Dallas", "Cowboys", "NFC", "East")
        self.washington = NFLTeam("Washington", "Commanders", "NFC", "East")
        self.eagles = NFLTeam("Philadelphia", "Eagles", "NFC", "East")
        self.giants = NFLTeam("New York", "Giants", "NFC", "East")

        # NFC West Teams
        self.seahawks = NFLTeam("Seattle", "Seahawks", "NFC", "West")
        self.rams = NFLTeam("Los Angeles", "Rams", "NFC", "West")
        self.cardinals = NFLTeam("Arizon", "Cardinals", "NFC", "West")
        self.sf49ers = NFLTeam("San Francisco", "49ers", "NFC", "West")

        # Create a list of all 32 NFLTeam objects
        self.allteams = [self.bengals, self.ravens, self.steelers, self.browns, 
                        self.texans, self.colts, self.titans, self.jaguars,
                        self.patriots, self.bills, self.dolphins, self.jets,
                        self.chiefs, self.broncos, self.raiders, self.chargers,
                        self.packers, self.bears, self.vikings, self.lions,
                        self.buccaneers, self.saints, self.panthers, self.falcons,
                        self.cowboys, self.washington, self.eagles, self.giants,
                        self.seahawks, self.rams, self.cardinals, self.sf49ers]

        # create 1 NFLTeam object to represent a Bye week
        # self.bye_team = NFLTeam("BYE", "BYE", None, None)
        # self.bye_team = NFLTeam(city=None, mascot=None, conference=None, division=None)

        # create Division objects (only accessible through the self.conferece.division notation)
        afc_n = Division("AFC", "North", [self.ravens, self.steelers, self.browns, self.bengals])
        afc_s = Division("AFC", "South", [self.texans, self.colts, self.titans, self.jaguars])
        afc_e = Division("AFC", "East",  [self.patriots, self.bills, self.dolphins, self.jets])
        afc_w = Division("AFC", "West",  [self.chiefs, self.broncos, self.raiders, self.chargers])
        nfc_n = Division("NFC", "North", [self.packers, self.bears, self.vikings, self.lions])
        nfc_s = Division("NFC", "South", [self.buccaneers, self.saints, self.panthers, self.falcons])
        nfc_e = Division("NFC", "East",  [self.cowboys, self.washington, self.eagles, self.giants])
        nfc_w = Division("NFC", "West",  [self.seahawks, self.rams, self.cardinals, self.sf49ers])

        # create confrence attributes
        self.afc = Conference("AFC", afc_n, afc_s, afc_e, afc_w)
        self.nfc = Conference("NFC", nfc_n, nfc_s, nfc_e, nfc_w)
        self.all_conferences = (self.afc, self.nfc)

        # create a list of all the divisions across the two conferences
        self.all_divisions = (self.afc.north, self.afc.south, self.afc.east, self.afc.west, 
                                 self.nfc.north, self.nfc.south, self.nfc.east, self.nfc.west)

    def create_teams(self) -> list:
        return
        # """ Returns a list of the 32 NFLTeam objects, one for each team"""
        # # AFC North Teams
        # ravens = NFLTeam("Baltimore", "Ravens", "AFC", "North")
        # steelers = NFLTeam("Pittsburgh", "Steelers", "AFC", "North")
        # browns = NFLTeam("Cleveland", "Browns", "AFC", "North")
        # bengals = NFLTeam("Cincinnati", "Bengals", "AFC", "North")

        # # AFC South Teams
        # texans = NFLTeam("Houston", "Texans", "AFC", "South")
        # colts = NFLTeam("Indianapolis", "Colts", "AFC", "South")
        # titans = NFLTeam("Tennessee", "Titans", "AFC", "South")
        # jaguars = NFLTeam("Jacksonville", "Jaguars", "AFC", "South")

        # # AFC East Teams
        # patriots = NFLTeam("New England", "Patriots", "AFC", "East")
        # bills = NFLTeam("Buffalo", "Bills", "AFC", "East")
        # dolphins = NFLTeam("Miami", "Dolphins", "AFC", "East")
        # jets = NFLTeam("New York", "Jets", "AFC", "East")

        # # AFC West Teams
        # chiefs = NFLTeam("Kansas City", "Chiefs", "AFC", "West")
        # broncos = NFLTeam("Denver", "Broncos", "AFC", "West")
        # raiders = NFLTeam("Las Vegas", "Raiders", "AFC", "West")
        # chargers = NFLTeam("Los Angeles", "Chargers", "AFC", "West")

        # # NFC North Teams
        # packers = NFLTeam("Green Bay", "Packers", "NFC", "North")
        # bears = NFLTeam("Chicago", "Bears", "NFC", "North")
        # vikings = NFLTeam("Minnesota", "Vikings", "NFC", "North")
        # lions = NFLTeam("Detroit", "Lions", "NFC", "North")

        # # NFC South Teams
        # buccaneers = NFLTeam("Tampa Bay", "Buccaneers", "NFC", "South")
        # saints = NFLTeam("New Orleans", "Saints", "NFC", "South")
        # panthers = NFLTeam("Carolina", "Panthers", "NFC", "South")
        # falcons = NFLTeam("Atlanta", "Falcons", "NFC", "South")

        # # NFC East Teams
        # cowboys = NFLTeam("Dallas", "Cowboys", "NFC", "East")
        # washington = NFLTeam("Washington", "Commanders", "NFC", "East")
        # eagles = NFLTeam("Philadelphia", "Eagles", "NFC", "East")
        # giants = NFLTeam("New York", "Giants", "NFC", "East")

        # # NFC West Teams
        # seahawks = NFLTeam("Seattle", "Seahawks", "NFC", "West")
        # rams = NFLTeam("Los Angeles", "Rams", "NFC", "West")
        # cardinals = NFLTeam("Arizon", "Cardinals", "NFC", "West")
        # sf49ers = NFLTeam("San Francisco", "49ers", "NFC", "West")

        # # Create a list of all 32 NFLTeam objects
        # teams = [patriots, bills, dolphins, jets, ravens, steelers, browns, bengals,
        #         texans, colts, titans, jaguars,chiefs, broncos, raiders, chargers,
        #         cowboys, washington, eagles, giants,packers, bears, vikings, lions,
        #         buccaneers, saints, panthers, falcons, seahawks, rams, cardinals, sf49ers]
        
        # # # create Division objects
        # # afc_n = Division("AFC", "North", [ravens, steelers, browns, bengals])
        # # afc_s = Division("AFC", "South", [texans, colts, titans, jaguars])
        # # afc_e = Division("AFC", "East",  [patriots, bills, dolphins, jets])
        # # afc_w = Division("AFC", "West",  [chiefs, broncos, raiders, chargers])
        # # nfc_n = Division("NFC", "North", [packers, bears, vikings, lions])
        # # nfc_s = Division("NFC", "South", [buccaneers, saints, panthers, falcons])
        # # nfc_e = Division("NFC", "East",  [cowboys, washington, eagles, giants])
        # # nfc_w = Division("NFC", "West",  [seahawks, rams, cardinals, sf49ers])
        # # # create Conference objects
        # # self.afc = Conference("AFC", afc_n, afc_s, afc_e, afc_w)
        # # self.nfc = Conference("NFC", nfc_n, nfc_s, nfc_e, nfc_w)

        # # create Division objects
        # self.afc_n = Division("AFC", "North", [ravens, steelers, browns, bengals])
        # self.afc_s = Division("AFC", "South", [texans, colts, titans, jaguars])
        # self.afc_e = Division("AFC", "East",  [patriots, bills, dolphins, jets])
        # self.afc_w = Division("AFC", "West",  [chiefs, broncos, raiders, chargers])
        # self.nfc_n = Division("NFC", "North", [packers, bears, vikings, lions])
        # self.nfc_s = Division("NFC", "South", [buccaneers, saints, panthers, falcons])
        # self.nfc_e = Division("NFC", "East",  [cowboys, washington, eagles, giants])
        # self.nfc_w = Division("NFC", "West",  [seahawks, rams, cardinals, sf49ers])
        # self.unique_divisions = (self.afc_n, self.afc_s, self.afc_e, self.afc_w, 
        #                          self.nfc_n, self.nfc_s, self.nfc_e, self.nfc_w)

        # # create confrence attributes
        # self.afc = Conference("AFC", self.afc_n, self.afc_s, self.afc_e, self.afc_w)
        # self.nfc = Conference("NFC", self.nfc_n, self.nfc_s, self.nfc_e, self.nfc_w)
        # self.conferences = (self.afc, self.nfc)

        # # NOTE: self.afc.north = self.afc_n

        # return teams

    def __str__(self):
        return self.allteams

    def get_teams(self, conf, div, names = False) -> list:
        """Returns a list of pointers to the NFLTeam objects in the specified conference and division. To get team names instead, set names = True

        Args:
            conf (str) a conference, i.e. "AFC", "NFC"
            div (str): a division, i.e. "north", "south", "east", "west"
            names (bool, optional): set True to return team names instead of object pointers. Defaults to True.

        Returns:
            list: _description_
        """
        if names:
            return [team.name for team in self.allteams if conf.lower() in team.conference.lower() and div.lower() in team.division.lower()]
        else:
            return [team for team in self.allteams if conf.lower() in team.conference.lower() and div.lower() in team.division.lower()]

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
                        # replace the default None value with the week_number of their bye
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
        
        ####################################################################################
        # (d) 
        # add the 6 divisional games to the  6 weeks for each division to play against themselves
        for conf in self.all_conferences:
            for div in conf.divisions:
                for team in div.allteams:
                    opps = [opp for opp in div.allteams if opp != team]
                    team.opponents.extend(opps*2)
                    team.rival_d6 = div

        # remove temp variables from namespace to help with debugging
        del conf, div, team, opps

        ####################################################################################
        # (icd) 
        # For each division, choose a division from the same conference that they will play against
        # __________________________________________________________________________________
        
        # do each loop within each conference
        for conf in self.all_conferences:
            # Get the 4 divisions in that conference and shuffle the order
            divs = conf.divisions.copy()
            random.shuffle(divs)

            # after random shuffling, first two divisions and last 2 divisions play each other in xcd games
            for icd_pair in (divs[:2], divs[2:]):
                div1 = icd_pair[0]
                div2 = icd_pair[1]

                # for teams in both divisions, add the teams from the other division to this team's list of opponents
                for team in div1.allteams:
                    team.opponents.extend(div2.allteams)
                    team.rival_icd4 = div2 
                for team in div2.allteams:
                    team.opponents.extend(div1.allteams)
                    team.rival_icd4 = div1

        # remove temp variables from namespace to help with debugging
        del conf, divs, team, div1, div2, icd_pair

        ####################################################################################
        # (xcd)
        # For each division, choose a division from the other conference that they will play against
        # for now, set it so that each team plays the same n/s/e/w from the other conference (i.e. AFC North plays NFC North...)
        # __________________________________________________________________________________

        # create a copy of the divisions in the other conference so that we can pop items from the list and avoid duplicate assignments
        xc_divs_copy = self.nfc.divisions.copy()
        random.shuffle(xc_divs_copy)
        
        for afc_div in self.afc.divisions:
            # pop one division from the other conference's div list, assign it as the xcd attribute for the AFC division's teams and vice versa.
            chosen_nfc_div = xc_divs_copy.pop()

            # assign the rival xc division for all 4 teams in the NFC division
            for team in chosen_nfc_div.allteams:
                team.rival_xcd4 = afc_div
                # add those 4 to the teams opponents list
                team.opponents.extend(team.rival_xcd4.allteams)

            # assign the rival xc division for all 4 teams in the AFC division
            for team in afc_div.allteams:
                team.rival_xcd4 = chosen_nfc_div
                # add those 4 to the teams opponents list
                team.opponents.extend(team.rival_xcd4.allteams)

        # for team in self.allteams:
        #     print(f"{team} -> {team.rival_xcd4} === {team.opponents}")
        del xc_divs_copy, afc_div, chosen_nfc_div, team

        ####################################################################################
        # (ic)
        # Get 2 new random teams from its own conference to play
        # in future, this should be changed to choose teams based on 
        # __________________________________________________________________________________


        for conf in self.all_conferences:
            for div in conf.divisions:
                for team in div.allteams:
                    while len(team.opponents) < 16:
                        available_divs = [div for div in conf.divisions if div not in [team.rival_d6, team.rival_icd4, team.rival_ic2]]
                        # if team.rival_ic2 == []:
                        #     team.rival_ic2 = available_divs
                        # elif len(available_divs) == 1:
                        #     team.rival_ic2.append(available_divs)

                        team.rival_ic2.append(available_divs[0])
                        new_opp = random.choice(available_divs[0].allteams)
                        team.opponents.append(new_opp)                       

                        if team not in new_opp.opponents:
                            new_opp.opponents.append(team)
                            new_opp.rival_ic2.append(div)

            h=0




            # for div in conf.divisions:
            #     for i in range(len(div.allteams)):
            #         team1 = div.allteams[i]

            #         # for each team in this division, identify the other 2 divisions in their conference that they haven't seen yet
            #         available_divs = [div for div in conf.divisions if div not in (team1.rival_d6, team1.rival_icd4)]
            #         team1.rival_ic2 = available_divs

            #         for other_div in available_divs:
            #             # choose one team from each of the 2 rival divisions. 
            #             new_opp = other_div.allteams[i]
            #             team1.opponents.append(new_opp)
            #             new_opp.opponents.append(team1)

            #             h=0


        ####################################################################################
        # xcd1
        # Establish 6 weeks for each division to play against themselves.
        # __________________________________________________________________________________








        return 

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
            teams_w_bye = [team for team in teams_list if "b" in team.schedule_outline[week].lower()]
            
            # assign cross-conference games
            teams_xc_game = [team for team in teams_list if team.schedule_outline[week] == "XC"]
            for team in teams_xc_game:
                pass
            