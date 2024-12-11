from spyne import ComplexModel, String, Integer, Float

class SongModel(ComplexModel):
    name = String
    artist = String
    release_date = String
    popularity = Integer
    length = Integer
    album = String
    song_id = String
    danceability = Float
    acousticness = Float
    energy = Float
    instrumentalness = Float
    liveness = Float
    valence = Float
    loudness = Float
    speechiness = Float
    tempo = Float
    key = String
    time_signature = String
    mood = String

