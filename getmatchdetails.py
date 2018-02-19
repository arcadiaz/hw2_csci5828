import requests
import time
import pandas as pd

target_skill_rating = ["NormalSkill/", "HighSkill/", "VeryHighSkill/"]
gamemode = ["AllPick/", "FunnyMode/"]
lobbytype = ["Public/","SoloMid/", "CoopBot/", "Ranked/"]

for lobby in lobbytype:
    for skill in target_skill_rating:
        for mode in gamemode:
            dir = lobby + mode + skill + 'matchhistory/'
            writedir = lobby + mode + skill + 'matchdetails/'
            if not os.path.exists(writedir):
                os.makedirs(writedir)
            for filename in os.listdir(dir):
                print(dir + filename)
                time.sleep(1)
		url = "<your url here>"
                result = requests.get(url).json()
                f = open(writedir + filename, 'w')
                f.write(str(result))
                f.close()

