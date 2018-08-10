import os
import logging
import subprocess
import kaggle
import json
import time
from kaggle import api


competitions = []


def comp_to_dict(competition):
    return {
        'ref': competition.ref,
        'deadline': str(competition.deadline),
        'category': competition.category,
        'reward': competition.reward,
        'teamCount': competition.teamCount,
        'userHasEntered': competition.userHasEntered
    }


print("Start downloading competitions")

for page in range(1, 16):
    print(page)
    time.sleep(10)
    comps = api.competitions_list(page=page)
    competitions.extend([comp_to_dict(c) for c in comps])


def file_to_dict(file):
    return {
        'name': file.name,
        'size': file.size,
        'creationDate': str(file.creationDate)
    }


print("Downloaded {} competitions".format(len(competitions)))
print("Start list files")

for competition in competitions:
    time.sleep(10)
    files = api.competition_list_files(competition['ref'])
    competition['files'] = [file_to_dict(f) for f in files]


s = json.dumps(competitions)

text_file = open("./metadata/competitions.json", "w")
text_file.write(s)
text_file.close()
