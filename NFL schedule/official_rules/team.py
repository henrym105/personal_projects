import numpy as np
import copy, json, random, time
import pandas as pd

class Conference():
    def __init__(self, name, n = None, s = None, e = None, w = None):
        self.name = name
        self.north = n
        self.south = s
        self.east = e
        self.west = w
        self.allteams = n.allteams + s.allteams + e.allteams + w.allteams
        self.divisions = [self.north, self.south, self.east, self.west]
    
    def __repr__(self) -> str:
        return f"CONFERENCE_{self.name}"

    def __str__(self) -> str:
        return self.__repr__()
        # return f"{self.name} class"

class Division():
    def __init__(self, conference_name, division_name, teams):

        self.conference = conference_name
        self.division = division_name
        self.allteams = teams
        self.unique_division = f"{self.conference[0]}.{self.division[0]}"

    def __repr__(self) -> str:
        return f"DIVISION_{self.unique_division}"

class NFLTeam():
    def __init__(self, city, mascot, conference, division):
        self.city = city
        self.mascot = mascot
        self.name = city + " " + mascot

        self.conference = conference
        self.division = division
        self.unique_division = f"{self.conference[0]}.{self.division[0]}"

        # pointers to the divisions that will be played in full
        # will extract teams from these divisions later on
        self.rival_d6 = self.unique_division
        self.rival_xcd4 = None
        self.rival_icd4 = None

        # pointers to the other divisions
        self.rival_ic2 = []
        self.rival_xcd1 = None

        self.schedule = {i: None for i in range(1,19)}
        self.schedule_outline = {i: None for i in range(1,19)}
        self.bye_week = None

        # this will be populated by the self.generate_opppnents list
        self.opponents = []
        self.games_to_play = []
        self.opponents_not_faced = []

        # self.required_opponents = {"division": None, "conference": None}

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"{self.mascot} {self.conference[0]}.{self.division[0]}"
    
    def set_bye_week(self, week_num):
        """assigns week_num (int) as the bye week"""
        self.bye_week = week_num
        self.schedule_outline[week_num] = "-B-"
        self.schedule[self.bye_week] = " -B-"     

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

    # def create_games(self):
    #     for opp in self.opponents:
    #         self.games_to_play.append(Game(self, opp, game_type=""))


class Game():
    """ Represents a game that is played between 2 teams """
    def __init__(self, home: NFLTeam, away: NFLTeam, game_type: str, week_num: int = -1, day = "sunday", time = 1):
        """
        Args:
            home (NFLTeam): the home team
            away (NFLTeam): the away team
            game_type (str): the type of game ("d6", "xcd4", "icd4", "ic2", "xcd1")
            week_num (int): the week in which this game is played. Defaults to -1
            day (str, optional): Defaults to "S".
            time (int, optional): Defaults to 1.
        """
        self.teams = set(home, away)
        self.hometeam = home
        self.awayteam = away

        self.type = game_type
        self.week = week_num
        self.day = day
        self.time = time

    def __repr__(self) -> str:
        return f"{self.away} @ {self.home}, {self.day}, {self.time}PM"

    def __str__(self) -> str:
        return self.__repr__()
