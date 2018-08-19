import os
import json
import time
from kaggle import api


text_file = open("../metadata/competitions.json", "r")
s = text_file.read()
text_file.close()

competitions = json.loads(s)

print(len(competitions))


def leaderboard_entry_to_dict(entry):
    return {
        'teamId': entry.teamId,
        'teamName': entry.teamName,
        'submissionDate': str(entry.submissionDate),
        'score': entry.score
    }


leaderboards = []

for c in competitions:
    print("Download {}".format(c['ref']))
    time.sleep(1)

    board = {}
    board['ref'] = c['ref']

    results = api.competition_leaderboard_view(c['ref'])

    board['top'] = [leaderboard_entry_to_dict(item) for item in results]
    board['best'] = None if len(
        board['top']) <= 0 else board['top'][0]['score']

    leaderboards.append(board)


s = json.dumps(leaderboards)

text_file = open("../metadata/leaderboards.json", "w")
text_file.write(s)
text_file.close()
