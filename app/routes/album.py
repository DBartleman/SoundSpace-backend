from flask import Blueprint, request
from ..models import db, User, Album

bp = Blueprint("albums", __name__, url_prefix="/artist/<int:artistid>")
searchbp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("/album/<int:albumid>")
# return one album
def get_album(albumid):
    album = Album.query.filter_by(id=albumid).first()
    data = {}
    data[album] = {
        "id": album.id,
        "artist_id": album.artist_id,
        "title": album.title,
        "description": album.description
    }
    return {"data": data}


@bp.route("/albums")
# return all favorite albums for a user
def get_favorites(userid):
    user = User.query.options(db.joinedload("favoriteAlbums")).filter_by(
        id=userid).first()
    favorite_ids = []
    albums = {}
    for album in user.favoriteAlbums:
        favorite_ids.append(album.id)
        albums[album.id] = {
            "id": album.id,
            "artist_id": album.artist_id,
            "title": album.title,
            "description": album.description
        }
    return {"albums": albums, "favoriteAlbums": favorite_ids}


@searchbp.route("/albums", methods=["POST"])
# search by album title
def search_albums():
    data = request.json
    searchQuery = data["searchQuery"]
    albums = Album.query.filter(Album.title.ilike(f"%{searchQuery}%"))
    result = [{
        "id": album.id,
        "artist_id": album.artist_id,
        "title": album.title,
        "description": album.description
    } for album in albums]
    return {"data": result}


