from app import app
from flask import Blueprint, request, jsonify, redirect
from ..models import db, User, Album
from app.util import token_required
from werkzeug.security import generate_password_hash
import jwt

bp = Blueprint('users', __name__, url_prefix='')


@bp.route('/signup', methods=['POST'])
def register_user():
    data = request.json
    hashed_password = generate_password_hash(data["password"])
    new_user = User(
        username=data["username"],
        email=data["email"],
        password=hashed_password
    )
    db.session.add(new_user)
    db.session.commit()
    token = jwt.encode(
        {"id": new_user.id, "username": new_user.username, "favoriteAlbums": [], "albums":{}}, app.config['SECRET_KEY'])
    return {'token': token.decode('UTF-8'), "id": new_user.id, "username": new_user.username}


@bp.route('/login', methods=['POST'])
def login_user():
    data = request.json
    print(data["username"])
    user = User.query.options(db.joinedload("favoriteAlbums")).filter_by(
        username=data['username']).first()
    if user.check_password(data['password']):
        fav_album_ids = []
        albums = {}
        for album in user.favoriteAlbums:
            fav_album_ids.append(album.id)
        token = jwt.encode(
            {"id": user.id, 
            "username": user.username, 
            "favoriteAlbums": fav_album_ids}, 
            app.config['SECRET_KEY']
        )
        return {'token': token.decode('UTF-8'), 
            "id": user.id, 
            "username": user.username, 
            "favoriteAlbums": fav_album_ids
        }
    else:
        return {'message': 'Invalid credentials'}, 401


# return user info
@bp.route("/users/<int:userid>")
@token_required
def profile_user(userid, current_user):
    user = User.query.filter_by(id=userid).first()
    data = [{
        "id": user.id,
        "username": user.username,
        "email": user.email,
    }]
    return {"data": data}
