from typing import List, Tuple
from datetime import date
from SongEntity import Song
import time
class songservice:
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def get_songs(self) -> List[Tuple[str, str, date, int, float]]:
        """
        Returns a list of tuples containing (name, artist, release_date, popularity, length) for each song.
        """
        return [(song.name, song.artist, song.release_date, song.popularity, song.length) for song in self.songs]

    def duration(self) -> str:
        """
        Calculate the total duration of all songs and return it in a human-readable format.
        - If under 60 minutes, return as minutes.
        - If 60 minutes or more, return as 'hrs min s'.
        """
        total_seconds = sum(song.length for song in self.songs)  # Total duration in seconds
        total_minutes = total_seconds // 60  # Convert to minutes
        if total_minutes < 60:
            return f"{int(total_minutes)} minutes"
        else:
            hours = total_seconds // 3600
            minutes = (total_seconds % 3600) // 60
            seconds = total_seconds % 60
            return f"{int(hours)} hrs {int(minutes)} min {int(seconds)} s"
