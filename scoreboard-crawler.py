import os
import logging
import subprocess
import kaggle
import json
import time

text_file = open("Output.json", "r")
s = text_file.read()
text_file.close()

comp = json.loads(s);

print(len(comp))
