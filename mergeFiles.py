import json
from os import listdir

dataFiles = listdir("data/")

bigFile = []

for dataFile in dataFiles:
    file = json.load(open(f"data/{dataFile}", encoding="utf8"))
    for song in file:
        currentSong = []
        if song['ms_played'] < 30000: # song listened to for more than 30s
            continue
        if song['episode_name'] == "None": # verify song isn't from a podcast
            continue
        if song['offline'] == True:
            continue
        currentSong.append(song['offline_timestamp'])
        currentSong.append(song['master_metadata_track_name'])
        currentSong.append(song['master_metadata_album_artist_name'])
        currentSong.append(song['master_metadata_album_album_name'])
        bigFile.append(currentSong)

with open('data.json', 'w', encoding='utf-8') as mergedFile:
    json.dump(bigFile, mergedFile, ensure_ascii=False)