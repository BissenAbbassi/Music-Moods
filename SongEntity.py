class Song:
    def __init__(self, name, artist, release_date, popularity, length, 
                 album="Unknown", song_id="Unknown", danceability=0.0, 
                 acousticness=0.0, energy=0.0, instrumentalness=0.0, 
                 liveness=0.0, valence=0.0, loudness=0.0, speechiness=0.0, 
                 tempo=0.0, key=0, time_signature=0, mood="Unknown"):
        self.name = name
        self.artist = artist
        self.release_date = release_date
        self.popularity = popularity
        self.length = length
        self.album = album
        self.song_id = song_id
        self.danceability = danceability
        self.acousticness = acousticness
        self.energy = energy
        self.instrumentalness = instrumentalness
        self.liveness = liveness
        self.valence = valence
        self.loudness = loudness
        self.speechiness = speechiness
        self.tempo = tempo
        self.key = key
        self.time_signature = time_signature
        self.mood = mood
