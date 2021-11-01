#%%
import sqlalchemy
import pandas as pd
from sqlalchemy.orm import sessionmaker
import  requests
import json
from datetime import datetime
import datetime
import sqlite3

#%%
DATABASE_LOCATION = 'sqlite:///my_played_tracks.sqlite'
USER_ID = 'yashi20'
TOKEN = "BQAN4cXlrIEdCGYyyIPvMOW8dhgPdMFDSwM7HFthjA_hRibJGGWW-PLyBOXucyKlX6TcYxgHAcXQd2K2x5kTooBb9e_ryW5oe0t0mYYzq1JV1CAkyLtKopfyGIlp7BymRIsBqLjxIzuA8FYR"

if __name__ == "__main__":

    headers = {
        "Accept": "application/json",
        'Content-Type': 'application/json',
        "Authorization": "Bearer {token}".format(token=TOKEN)
    }

    today = datetime.datetime.now() 
    yesterday = today - datetime.timedelta(days=1)
    yesterday_unix_timestamp = int(yesterday.timestamp()) #* 10000
    print(yesterday_unix_timestamp)

    r = requests.get("https://api.spotify.com/v1/me/player/recently-played", headers = headers, params = {"after" : yesterday_unix_timestamp})

    data = r.json()

    print(data)

# %%
song_names = []
artist_names = []
played_at_list = []
timestamps = []

for song in data["items"]:
    song_names.append(song["track"]["name"])
    artist_names.append()
    played_at_list.append(song["played_at"])
    timestamps.append()

played_at_list
# %%
