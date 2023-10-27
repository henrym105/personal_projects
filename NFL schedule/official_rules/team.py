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

