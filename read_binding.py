import json

data = {}

fin = 'test_buttons_1.txt'

with open(fin, 'r') as f:
    data = json.load(f)

print data
