import json

words = {}

with open('./data/scowlwords.txt', 'r') as text_file:
    for line in text_file.readlines():
        line = line.rstrip('\n')
        words[line] = 1

with open('./data/scowlwords.json', 'w') as json_file:
    data = json.dumps(words)
    json_file.writelines(data)
