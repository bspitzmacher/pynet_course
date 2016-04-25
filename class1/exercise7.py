# Class 1: Exercise 7
import yaml
import json

with open("exercise6.yml") as f:
    yaml_list = yaml.load(f)

with open("exercise6.json") as j:
    json_list = json.load(j)

from pprint import pprint as pp
pp(yaml_list)
pp(json_list)
