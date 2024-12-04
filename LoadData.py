import pandas as pd
from datetime import datetime
from typing import List
from datetime import date

class Loaddata:
    def __init__(self, csv_path: str):
        self.csv_path = csv_path
        self.songs: List[Song] = []  # Initialize an empty list for Song objects

    def load_songs_from_csv(self):
        """
        Reads songs from a CSV file using Pandas and populates the `songs` list.
        Assumes the CSV file contains columns matching the Song attributes.
        """
        try:
            # Read the CSV file into a Pandas DataFrame
            df = pd.read_csv(self.csv_path)

            # Iterate over the DataFrame rows and create Song objects
            for _, row in df.iterrows():
                song = Song(
                    name=row["name"],
                    album=row["album"],
                    artist=row["artist"],
                    song_id=row["id"],
                    release_date=datetime.strptime(row["release_date"], "%Y-%m-%d").date(),
                    popularity=int(row["popularity"]),
                    length=float(row["length"]),
                    danceability=float(row["danceability"]),
                    acousticness=float(row["acousticness"]),
                    energy=float(row["energy"]),
                    instrumentalness=float(row["instrumentalness"]),
                    liveness=float(row["liveness"]),
                    valence=float(row["valence"]),
                    loudness=float(row["loudness"]),
                    speechiness=float(row["speechiness"]),
                    tempo=float(row["tempo"]),
                    key=int(row["key"]),
                    time_signature=int(row["time_signature"]),
                    mood=row["mood"],
                )
                self.songs.append(song)

        except FileNotFoundError:
            print(f"Error: File not found at path {self.csv_path}.")
        except KeyError as e:
            print(f"Error: Missing column in CSV file: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            

if __name__ == "__main__":
    # Path to the CSV file
    csv_file_path =r"C:/Users/Bisse/Desktop/soc-projet/cleaned_data_moods.csv"

    # Initialize and run the main program
    main_app = Loaddata(csv_file_path)
    main_app.load_songs_from_csv()
    print(main_app.songs)           