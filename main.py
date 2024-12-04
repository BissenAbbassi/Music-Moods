from LoadData import Loaddata
from SongService import songservice


class Main:
    def __init__(self, csv_path: str):
        self.loader = Loaddata(csv_path)  # Initialize the LoadData object
        self.song_service = songservice()  # Initialize the SongService object

    def run(self):
        # Step 1: Load data from CSV
        print("Loading songs from CSV...")
        self.loader.load_songs_from_csv()
        if not self.loader.songs:
            print("No songs found. Exiting program.")
            return

        # Step 3: Display all songs (name, artist, release_date, popularity, length)
        print("\nAvailable Songs:")
        songs_list = self.song_service.get_songs()
        for song in songs_list:
            name, artist, release_date, popularity, length = song
            print(f"Name: {name}, Artist: {artist}, Release Date: {release_date}, "
                  f"Popularity: {popularity}, Length: {length:.2f} seconds")

        # Step 4: Calculate total duration of all songs
        total_duration = self.song_service.duration()
        print(f"\nTotal Duration of All Songs: {total_duration:.2f} seconds")


# Example Usage:
if __name__ == "__main__":
    # Path to the CSV file
    csv_file_path =r"C:/Users/Bisse/Desktop/soc-projet/cleaned_data_moods.csv"

    # Initialize and run the main program
    main_app = Main(csv_file_path)
    main_app.run()
