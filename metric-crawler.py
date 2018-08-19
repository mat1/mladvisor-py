import requests
import re
import os
import json

text_file = open("./metadata/competitions.json", "r")
s = text_file.read()
text_file.close()

competitions = json.loads(s)

print(len(competitions))

metrics = []
errors = []

for c in competitions:
    print("Download metric for {}".format(c['ref']))

    r = requests.get(
        'https://www.kaggle.com/c/{}/leaderboard'.format(c['ref']))
    content = r.text
    pattern = r'evaluationAlgorithm\":({[^{}]+})'
    m = re.search(pattern, content)

    if m != None and (len(m.groups()) == 1):
        metric_string = m.group(1)
        metric = json.loads(metric_string)
        metric['ref'] = c['ref']

        metrics.append(metric)
    else:
        print("Error with {}".format(c['ref']))
        errors.append(c['ref'])

print(metrics)

s = json.dumps(metrics)

text_file = open("./metadata/metrics.json", "w")
text_file.write(s)
text_file.close()

print(errors)
