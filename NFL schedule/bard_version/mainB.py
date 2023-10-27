import gurobipy as gp

class NFLScheduleOptimizer:
    def __init__(self, teams, divisions, conferences):
        self.teams = teams
        self.divisions = divisions
        self.conferences = conferences

        # Create a model
        self.model = gp.Model()

        # Create decision variables
        self.game_vars = {}
        for team1 in self.teams:
            for team2 in self.teams:
                for week in range(1, 18):
                    for timeslot in range(1, 5):
                        for home_away in range(2):
                            self.game_vars[(team1, team2, week, timeslot, home_away)] = self.model.addVar(vtype=gp.GRB.BINARY)

        # Add constraints

        # Each team must play 16 games, 8 at home and 8 away
        for team in self.teams:
            self.model.addConstr(gp.quicksum([self.game_vars[(team, opponent, week, timeslot, home_away)] for opponent in self.teams for week in range(1, 18) for timeslot in range(1, 5) for home_away in range(2)]) == 16)

        # Each team must play all of the teams in its division twice, once at home and once away
        for division in self.divisions:
            for team in self.teams:
                for opponent in self.teams:
                    if team != opponent and opponent in division:
                        self.model.addConstr(self.game_vars[(team, opponent, week, timeslot, home_away)] + self.game_vars[(opponent, team, week, timeslot, (1 - home_away))] == 2)

        # Each team must play 4 games against teams from the other division in its conference, 2 at home and 2 away
        for conference in self.conferences:
            for team in self.teams:
                for opponent in self.teams:
                    if team != opponent and opponent not in self.divisions[team]:
                        self.model.addConstr(self.game_vars[(team, opponent, week, timeslot, home_away)] + self.game_vars[(opponent, team, week, timeslot, (1 - home_away))] == 2)

        # Each team must play 4 games against teams from the opposite conference, 2 at home and 2 away
        for team in self.teams:
            for opponent in self.teams:
                if team != opponent and opponent not in self.conferences[team]:
                    self.model.addConstr(self.game_vars[(team, opponent, week, timeslot, home_away)] + self.game_vars[(opponent, team, week, timeslot, (1 - home_away))] == 2)

        # No team can play the same team in back-to-back weeks
        for team1 in self.teams:
            for team2 in self.teams:
                for week1 in range(1, 17):
                    for week2 in range(week1 + 1, 18):
                        for timeslot in range(1, 5):
                            for home_away in range(2):
                                self.model.addConstr(self.game_vars[(team1, team2, week1, timeslot, home_away)] + self.game_vars[(team2, team1, week2, timeslot, (1 - home_away))] <= 1)

        # No team can play more than 3 games in a row at home or away
        for team in self.teams:
            for home_away in range(2):
                for week1 in range(1, 16):
                    for week2 in range(week1 + 1, 17):
                        for week3 in range(week2 + 1, 18):
                            self.model.addConstr(self.game_vars[(team, opponent, week1, timeslot, home_away)] + self.game_vars[(team, opponent, week2, timeslot, home_away)] + self.game_vars[(team, opponent, week3, timeslot, home_away)] <= 2)

        # No team can play more than 7 consecutive games without a bye week
        for team in self.teams:
            for week1 in range(1, 18):
                for week2 in range(week1 + 1, 19):
                    for timeslot in range(1, 5):
                        for home_away in range(2):
                            self.model.addConstr(self.game_vars[(team, opponent, week1, timeslot, home_away)] + self.game_vars[(team, opponent, week2, timeslot, home_away)] <= 1)

        # Solve the model
        self.model.optimize()

        # Extract the schedule
        self.schedule = {}
        for team1 in self.teams:
            for team2 in self.teams:
                for week in range(1, 18):
                    for timeslot in range(1, 5):
                        for home_away in range(2):
                            if self.game_vars[(team1, team2, week, timeslot, home_away)].x > 0:
                                self.schedule[(team1, team2, week, timeslot, home_away)] = True

        return self.schedule

# Example usage:

teams = ["Patriots", "Bills", "Dolphins", "Jets", "AFC East"]
divisions = [[teams[0], teams[1], teams[2]], [teams[3], teams[4], teams[5]]]
conferences = [[divisions[0], divisions[1]], [divisions[2], divisions[3]]]

optimizer = NFLScheduleOptimizer(teams, divisions, conferences)

schedule = optimizer.optimize()

# Print the schedule
for team1, team2, week, timeslot, home_away in sorted(schedule.keys()):
    if schedule[(team1, team2, week, timeslot, home_away)]:
        print(f"{team1} vs. {team2} at {timeslot} on Week {week}")