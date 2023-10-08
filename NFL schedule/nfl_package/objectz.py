import copy, json, random

class NFLSchedule():
    """
    Holds the master schedule for the NFL Season, optional parameter weeks set to default = 16
    """
    def __init__(self, weeks = 18):
        self.schedule = {}

    def __str__(self):
        return json.dumps(self.schedule, indent=4)

    def add_matchup(self, week, hometeam, awayteam):
        self.schedule[week] = {"home": hometeam, "away": awayteam}


class NFLTeam():

    def __init__(self, name, conference, division):
        self.name = name
        self.conference = conference
        self.division = division
        self.bye_week = None
        self.games_played = 0
        self.division_games_played = 0
        self.conference_games_played = 0
        self.schedule = {i: None for i in range(0,19)}
        self.opponents_not_faced = []

    def __repr__(self):
        return f"{self.name} {self.conference}.{self.division[0].lower()}"

    def __str__(self):
        # return f"{self.name} ({self.conference} {self.division}) - Bye Week: {self.bye_week} - Games Played: {self.games_played}"
        return self.__repr__()

    def play_game(self, opponent, week_number, home_indicator):
        self.games_played += 1

        if opponent.conference == self.conference:
            self.conference_games_played += 1
            if opponent.division == self.division:
                self.division_games_played += 1

        # delete the opponent from the list of other teams that this team has not played against
        self.opponents_not_faced.remove(opponent)

        # add this game to the team objects schedule
        self.schedule.append({
            'week': week_number,
            'opponent': opponent,
            'home_game': home_indicator  # You can determine if it's a home game based on your scheduling logic
        })

    def add_game(self, week, opponent):
        self.schedule[int(week)] = opponent
        

    def set_bye_week(self, week_num):
        self.bye_week = week_num
        self.schedule[self.bye_week] = " -- BYE WEEK --"
