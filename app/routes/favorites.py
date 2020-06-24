from flask import Blueprint, request
from ..models import db, Album, User, Favorite

bp = Blueprint("favorites", __name__, url_prefix="")


@bp.route("/<int:userid>/albums/favorites")
# return favorite albums for a user
def get_favorites(userid):
    favorites = Favorite.query.options(db.joinedload(
        "favalbums")).filter_by(user_id=userid).all()

    data = [
        favorite.album_id
        for favorite in favorites]
    return {"data": data}


@bp.route("/<int:userid>/<int:albumid>/favorites", methods=['POST'])
# push an album into favorites
# I might not need user id in the route since its just the currently logged in user (?)
def post_favorites(userid, albumid):
    data = request.json
    album = Album.query.filter_by(id=albumid).first()
    favorites = Favorite(**data)
    db.session.add(favorites)
    db.session.commit()
    albums = {}
    fave = {}
    fave[favorites.id] = {"album_id": album.id}
    albums[album.id] = {
        "id": album.id,
        "artist_id": album.artist_id,
        "title": album.title,
        "description": album.description
    }
    return {
        "albums": albums,
        "fave": favorites.album_id
    }


@bp.route("/<int:userid>/<int:albumid>/favoritedelete", methods=['DELETE'])
# remove an album from favorites
def delete_favorites(userid, albumid):
    data = request.json # unused?
    favorite = Favorite.query.filter_by(user_id=userid, album_id=albumid).first()
    db.session.delete(favorite)
    db.session.commit()
    user = User.query.options(db.joinedload("favoriteAlbums")).filter_by(
        id=userid).first()
    fav_album_ids = []
    albums = {}
    for album in user.favoriteAlbums:
        fav_album_ids.append(album.id)
        albums[album.id] = {
            "id": album.id,
            "artist_id": album.artist_id,
            "title": album.title,
            "description": album.description
        }
    return {"albums": albums, "favoriteAlbums": fav_album_ids}
