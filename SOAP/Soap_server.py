from spyne import Application, rpc, ServiceBase, Unicode, Integer, Float, Array
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server
from SongEntity import Song
from LoadData import Loaddata
from SongService import songservice

# Load song data
loader = Loaddata('cleaned_data_moods.csv')
loader.load_songs_from_csv()
service = songservice(loader.songs)

class SongService(ServiceBase):
    @rpc(_returns=Array(Unicode))
    def get_songs(ctx):
        """Return all songs as a SOAP response."""
        songs = service.get_songs()
        return [
            f"{s[0]} by {s[1]} - Released on {s[2]}" for s in songs
        ]

    @rpc(Unicode, Integer, _returns=Array(Unicode))
    def recommend_songs(ctx, mood, limit):
        """Recommend songs based on mood."""
        songs = service.recommend_songs(mood, limit)
        return [
            f"{song.name} by {song.artist}" for song in songs
        ]

# Define the namespace for the SOAP service
namespace = "http://localhost/songs"

# Create the SOAP application
soap_app = Application(
    [SongService],
    namespace,
    in_protocol=Soap11(),
    out_protocol=Soap11()
)

# Run the WSGI server
if __name__ == "__main__":
    server = make_server('0.0.0.0', 8000, WsgiApplication(soap_app))
    print("SOAP server running on http://0.0.0.0:8000")
    server.serve_forever()
