import pylast, json, os, time

LASTFM_API_KEY = os.environ.get('API_KEY')
LASTFM_API_SECRET = os.environ.get('API_SECRET')
LASTFM_USERNAME = os.environ.get('USERNAME')
LASTFM_PASSWORD = pylast.md5(os.environ.get('PASSWORD'))

network = pylast.LastFMNetwork(api_key=LASTFM_API_KEY, api_secret=LASTFM_API_SECRET, username=LASTFM_USERNAME, password_hash=LASTFM_PASSWORD)

dataBlocks = os.listdir("D:\\code\\spotifyData\\blocks\\")

for block in dataBlocks:
    with open(f"D:\\code\\spotifyData\\blocks\\{block}", encoding='utf-8') as file:
        jsonFile = json.load(file)
        for song in jsonFile:
            try:
                print(f"trying to scrobble {song[2]} - {song[1]} ...")
                api_call = network.scrobble(song[2], song[1], int(time.time()))
                print(f"scrobbled {song[2]} - {song[1]}")
            except Exception as e:
                print(f"whoopsies!! there was an ewwor >///< ({e})")