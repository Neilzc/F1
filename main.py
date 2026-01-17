import fastf1
from fastf1 import plotting
import pandas as pd

race_year = 2025

session = fastf1.get_session(2025, 'Monaco', 'R')
teams = plotting.list_team_names(session)


team_drivers_map = {}

for team in teams:
    team_drivers_map[team] = plotting.get_driver_names_by_team(team, session)

print(team_drivers_map)

