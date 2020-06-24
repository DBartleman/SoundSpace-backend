from flask import Flask, render_template, redirect
from .config import Config
from .models import db
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
Migrate(app, db)
CORS(app)

from .routes import user, song, album, artist, favorites  # noqa
app.register_blueprint(user.bp)
app.register_blueprint(song.bp)
app.register_blueprint(album.bp)
app.register_blueprint(artist.bp)
app.register_blueprint(favorites.bp)
# app.register_blueprint(song.searchbp)
app.register_blueprint(album.searchbp)
# app.register_blueprint(artist.searchbp)
