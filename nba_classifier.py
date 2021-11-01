import nba_stats_rework as nsr
import os

directory = "/Users/macowner/Documents/Hello/NBA_Predictor/Predictor_csv_files/"
start, end = int(input("Type in a start year for the search: ")), int(input("Type in an end year: "))
years = range(start,end+1)
tpg = []
opp_per_game = []
team_per_100 = []
opp_per_game = []
team_advanced = []
team_shooting = []

for i in years:
    tpg.append(nsr.nbastats(i).team_per_game())
    with open(directory + "{}_team_per_game.txt".format(i), "w") as f1:
        f1.write(tpg[i-start].to_csv())
'''
for i in years:
    opg = nsr.nbastats(i).opp_per_game()
for i in years:
    tp100 = nsr.nbastats(i).team_per_100()
for i in years:
    op100 = nsr.nbastats(i).opp_per_100()
for i in years:
    advanced = nsr.nbastats(i).team_advanced()
for i in years:
    tsh = nsr.nbastats(i).team_shooting()
for i in years:
    osh = nsr.nbastats(i).opp_shooting()
'''