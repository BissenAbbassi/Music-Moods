from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from LoadData import Loaddata
from SongService import songservice
from typing import List

app = FastAPI()

# Load songs and initialize the service
csv_file_path = "cleaned_data_moods.csv"
loader = Loaddata(csv_file_path)
loader.load_songs_from_csv()
song_service = songservice(loader.songs)


@app.get("/songs")
def get_songs():
    """Return all songs."""
    return song_service.get_songs()


@app.get("/recommendations")
def get_recommendations(mood: str, limit: int = Query(None, description="Number of recommendations to return")):
    """Return recommended songs based on mood."""
    recommendations = song_service.recommend_songs(mood, limit)
    if recommendations:
        return recommendations
    return JSONResponse(status_code=404, content={"message": "No recommendations found for the given mood."})


@app.get("/duration")
def get_duration():
    """Return the total duration of all songs."""
    total_duration = song_service.duration(song_service.songs)
    return {"total_duration": total_duration}


@app.get("/acousticness-energy")
def acousticness_vs_energy():
    """Generate and show Acousticness vs Energy scatter plot."""
    song_service.acousticness_vs_energy()
    return {"message": "Acousticness vs Energy plot displayed."}


@app.get("/latest-songs")
def get_latest_songs(limit: int = Query(None, description="Number of latest songs to return")):
    """Return the latest songs by release date."""
    latest = song_service.latest_songs(limit)
    return latest


@app.get("/aggregated-stats")
def get_aggregated_stats():
    """Return aggregated statistics by mood."""
    stats = song_service.aggregated_stats_by_mood()
    return stats


@app.get("/most-popular-song")
def most_popular_song():
    """Return the most popular song."""
    return song_service.most_popular_song()


@app.get("/longest-song")
def longest_song():
    """Return the longest song."""
    return song_service.longest_song()


@app.get("/shortest-song")
def shortest_song():
    """Return the shortest song."""
    return song_service.shortest_song()


@app.get("/recommendations-duration")
def recommendations_duration(mood: str, limit: int = Query(None, description="Number of recommendations to consider")):
    """Return the total duration and list of recommended songs."""
    filtered_list = song_service.recommend_songs(mood, limit)
    duration = song_service.duration(filtered_list)
    return {
        "total_songs": len(filtered_list),
        "total_duration": duration,
        "songs": filtered_list,
    }
