import requests
import json

def rotation(champs, api):
    response = requests.get("https://eun1.api.riotgames.com/lol/platform/v3/champion-rotations?api_key=" + api)
    if response.status_code != 200:
        print("An error occured :(")
        print("Status code:" + str(response.status_code))
    else:
        data = response.json()
        for x in data['freeChampionIds']:
            for champion in champs['data']:
                if champs['data'][champion]['key'] == str(x):
                    print(champion)
                    break

champ_file = open('champion.json','r')
champs = json.load(champ_file)
champ_file.close()

config_file = open('config.json','r')
config = json.load(config_file)
api = config['api']
username = config['username']
config_file.close()

print("***LOL STATS TRACKER FOR EUNE***")
print("MADE BY PAWEL ROSTECKI\n")
print("WELCOME " + username)
print("CURRENT ROTATION:")

rotation(champs, api)
