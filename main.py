from SongService import songservice
from LoadData import Loaddata
import csv
class Main:
    def __init__(self, csv_path: str):
        # Initialize the loader and load songs from the CSV
        self.loader = Loaddata(csv_path)
        self.loader.load_songs_from_csv()  # Ensure this method loads data into self.loader.songs

        # Pass the loaded songs to the songservice constructor
        self.song_service = songservice(self.loader.songs)

    def run(self):
        # Step 1: Check if songs are loaded
        if not self.loader.songs:
            print("No songs found. Exiting program.")
            return

        # Step 2: Display all songs
        print("\nAvailable Songs:")
        songs_list = self.song_service.get_songs()
        for song in songs_list:
            name, artist, release_date, popularity, length = song
            print(f"Name: {name}, Artist: {artist}, Release Date: {release_date}, "
                  f"Popularity: {popularity}, Length: {length:.2f} seconds")

        # Step 3: Calculate total duration of all songs
        total_duration = self.song_service.duration()
        print(f"\nTotal Duration of All Songs: {total_duration}")


if __name__ == "__main__":
    # Path to the CSV file
    csv_file_path = "cleaned_data_moods.csv"
    
    # Create the Main application object and run it
    main_app = Main(csv_file_path)
    main_app.run()
