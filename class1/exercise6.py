# Class 1: Exercise 6
import yaml
import json

my_list = range(10)
my_list.append('hello')
my_list.append('world')
my_list.append({})
my_list[-1]
my_list[-1]['hostname'] = 'CORP-FW-01'
my_list[-1]['ip_addr'] = '10.1.1.2'
my_list[-1]['sub_mask'] = '255.255.255.0'
my_list[-1]['attribs'] = range(5)
my_list[-1]['new_key'] = 'cisco'
my_list[-1]['new_key2'] = 'arista'

print(my_list)

with open("exercise6.yml", "w") as f:
	f.write(yaml.dump(my_list, default_flow_style=False))
	
with open("exercise6.json", "w") as f:
	json.dump(my_list, f)
