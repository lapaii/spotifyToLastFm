# spotify to last fm

### steps to use:
1. create an api app at https://www.last.fm/api/accounts
2. create a .env file and fill out the data as specified below

```
API_KEY=[LAST FM API KEY]
API_SECRET=[LAST FM SHARED SECRET]
USERNAME=[LAST FM USERNAME]
PASSWORD=[LAST FM PASSWORD (must be plaintext)]
```

3. copy all your ```Streaming_History_Audio_YEAR-YEAR_INDEX.json``` files into a new folder called data
4. create a new folder called blocks (dont put anything there)
5. run ```mergeFiles.py```
6. ensure that it creates a ```data.json``` file in the main folder
7. run ```splitFile.py``` to split it into 2800 song 'blocks' (last fm scrobble limit per day)
8. run ```scrobble.py``` (you will have to run it multiple times as it only scrobbles one 'block' at a time)

please open any issues if theres problems with it !!! i will try my best to fix stuff (within reason)
