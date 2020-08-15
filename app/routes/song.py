from flask import Blueprint, request
from ..models import Song, db, Album


bp = Blueprint("songs", __name__, url_prefix="")


@bp.route("/songs")
def get_songs():
    songs = Song.query.all()
    data = [{
        "id": song.id,
        "album_id": song.album_id,
        "url": song.url,
        "cover": song.cover
    } for song in songs]
    return {"data": data}


@bp.route("/songs/<albumid>")
def get_songs_by_album(albumid):
    songs = Song.query.filter_by(album_id=albumid).all()
    data = {}
    for song in songs:
        data[song.id] = {
            "id": song.id,
            "album_id": song.album_id,
            "url": song.url
        }
    return {"data": data}


@bp.route("/songs/<int:albumid>/<int:songid>")
# may go unused
def get_song_in_album(albumid, songid):
    song = Song.query.filter_by(album_id=albumid).filter_by(id=songid).first()
    data = {
        "id": song.id,
        "album_id": song.album_id,
        "url": song.url
    }
    return {"data": data}

