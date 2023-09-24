import requests
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('word')
args = parser.parse_args()
word = args.word
print(word)

url = 'https://api.dictionaryapi.dev/api/v2/entries/en/'
response = requests.get(url + word)
info = response.json()

for i in info[0]['meanings'][0]['definitions']:
    print(json.dumps(info[0]['meanings'][0]['definitions'][i]['definition'], indent=2))