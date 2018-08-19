import os
import json
import time
from kaggle import api


text_file = open("../metadata/competitions.json", "r")
s = text_file.read()
text_file.close()

competitions = json.loads(s)

print(len(competitions))

for c in competitions:
    print("Download scoreboard for {}".format(c['ref']))
    time.sleep(1)
    api.competition_leaderboard_download(c['ref'], '../scoreboards')
