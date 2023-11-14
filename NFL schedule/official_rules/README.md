This package has been designed to create the NFL schedule according to most of the rules actually used to create the real thing. 

source: [Creating the NFL Schedule](https://operations.nfl.com/gameday/nfl-schedule/creating-the-nfl-schedule/)

### Here are the rules:
- 32 teams in the league
    - Divided into 2 confereneces: AFC, NFC
    - Each conference has 4 divisions (north, south, east, west)
    - Each division has 4 teams

- 18 weeks in the regular season. 
    - Each team has 1 bye week (must be in weeks 4 to 14)
        - equal number of teams from AFC and NFC have a bye on any given week
    - Each team plays 17 games
        - 6 games are within their division --> play the other 3 teams twice: 1 home, 1 away 
        - 4 games are against the teams from a different division in the same conference (2 home, 2 away)
        - 4 games are against the teams from any division in the other coference (2 home, 2 away)
        - 2 games against the remaining teams in its own conference, based on division ranking from the previous season. 
        - 1 game against a non conference opponent from a division that the team is not scheduled to play


#### Long term constraints to implement later:
- Every team plays each of the other 31 teams at least once every 4 years
    - because each team rotates through playing the 4 teams in a x_conf division each year
- Last year's Super Bowl champion plays at home for the week 1 Thursday night game that kicks off the new season.
- International games






