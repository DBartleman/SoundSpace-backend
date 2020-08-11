from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash
from sqlalchemy import Table

db = SQLAlchemy()


class Favorite(db.Model):
    __tablename__ = "favorite"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    song_id = db.Column(db.Integer, db.ForeignKey("albums.id"), nullable=False)


class User(db.Model):
    __tablename__ = "users"

    def check_password(self, password):
        return check_password_hash(self.password, password)

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

    favoriteAlbums = db.relationship(
        "Album", secondary="favorite")


class Artist(db.Model):
    __tablename__ = "artists"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=False)
    description = db.Column(db.String(500), nullable=True, unique=False)

    albums = db.relationship("Album", back_populates="artist")


class Album(db.Model):
    __tablename__ = "albums"

    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey("artists.id"), nullable=False)
    title = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(1000))

    songs = db.relationship("Song", back_populates="album")
    artist = db.relationship("Artist", back_populates="albums")
    favorites = db.relationship("Favorite")


class Song(db.Model):
    __tablename__ = "songs"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    album_id = db.Column(db.Integer, db.ForeignKey("albums.id"), nullable=False)
    url = db.Column(db.String(200), nullable=False)
    cover = db.Column(db.String(200), nullable=False)
    
    album = db.relationship("Album", back_populates="songs")




