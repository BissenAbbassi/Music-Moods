import csv
from typing import List

from SongEntity import Song


class Loaddata:
    def __init__(self, csv_path: str):
        self.csv_path = csv_path
        self.songs: List[Song] = []  # Initialize an empty list for songs

    def load_songs_from_csv(self):
        with open(self.csv_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.songs.append(Song(
                    name=row['name'],
                    artist=row['artist'],
                    release_date=row['release_date'],
                    popularity=int(row['popularity']),
                    length=float(row['length'])
                ))
