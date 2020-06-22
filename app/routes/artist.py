from app import app
from flask import Blueprint
from ..models import db, Artist


bp = Blueprint('artists', __name__, url_prefix='')


@bp.route("/artists/<int:artistid>")
def profile_artist(artistid):
    artist = Artist.query.filter_by(id=artistid).first()
    data = [{
        "id": artist.id,
        "description": artist.description
    }]
    return {"data": data}
