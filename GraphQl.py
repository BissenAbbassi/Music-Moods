from fastapi import FastAPI
from ariadne import QueryType, make_executable_schema
from ariadne.asgi import GraphQL
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from LoadData import Loaddata
from SongService import songservice


type_defs = """
type Song {
    name: String!
    artist: String!
    release_date: String!
    popularity: Int!
    length: Int!
    mood: String!
    acousticness: Float
    energy: Float
}

type Query {
    allSongs: [Song!]
    recommendSongs(mood: String!, limit: Int): [Song!]
    aggregatedStats: [String!]
    mostPopularSong: String!
    longestSong: String!
    shortestSong: String!
}
"""

query = QueryType()

csv_file_path = "cleaned_data_moods.csv"
loader = Loaddata(csv_file_path)
loader.load_songs_from_csv()
song_service = songservice(loader.songs)

@query.field("allSongs")
def resolve_all_songs(_, info):
    return song_service.get_songs()

@query.field("recommendSongs")
def resolve_recommend_songs(_, info, mood, limit=None):
    return song_service.recommend_songs(mood, limit)

@query.field("aggregatedStats")
def resolve_aggregated_stats(_, info):
    return song_service.aggregated_stats_by_mood()

@query.field("mostPopularSong")
def resolve_most_popular_song(_, info):
    return song_service.most_popular_song()

@query.field("longestSong")
def resolve_longest_song(_, info):
    return song_service.longest_song()

@query.field("shortestSong")
def resolve_shortest_song(_, info):
    return song_service.shortest_song()

schema = make_executable_schema(type_defs, query)

app = FastAPI()
app.add_route("/graphql", GraphQL(schema, debug=True))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8082)
