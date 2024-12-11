from zeep import Client

wsdl_url = 'http://0.0.0.0:8000/?wsdl'
client = Client(wsdl=wsdl_url)

# Get all songs
songs = client.service.GetSongs()
print("Songs:", songs)

# Recommend songs
recommended_songs = client.service.RecommendSongs(mood="happy", limit=3)
print("Recommended Songs:", recommended_songs)
