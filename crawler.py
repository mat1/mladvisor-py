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


for page in range(1, 3):
    time.sleep(5)
    comps = api.competitions_list(page=page)
    competitions.extend([comp_to_dict(c) for c in comps])


def file_to_dict(file):
    return {
        'name': file.name,
        'size': file.size,
        'creationDate': str(file.creationDate)
    }


for competition in competitions:
    time.sleep(5)
    files = api.competition_list_files(competition['ref'])
    competition['files'] = [file_to_dict(f) for f in files]


s = json.dumps(competitions)
print(s)
