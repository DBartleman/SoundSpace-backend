from app.models import User, Artist, Album, Song, Favorite
from app import app, db
from dotenv import load_dotenv
load_dotenv()

with app.app_context():
    db.drop_all()
    db.create_all()
    
    # Demo user
    user = User(email="demo@email.com", username="demo", password="demo")

    # artists
    artist1 = Artist(
        name="Air", description="Air are a French music duo from Versailles, consisting of Nicolas Godin and Jean-Benoît Dunckel.")
    artist2 = Artist(name="The Seatbelts", description="")
    artist3 = Artist(name="Fred Hersch", description="")
    artist4 = Artist(name="Gregory Privat", description="")
    artist5 = Artist(name="Jim Lang", description="")
    artist6 = Artist(name="Kat Epple and Bob Stohl", description="")
    artist7 = Artist(name="Maxis", description="")
    artist8 = Artist(name="Michael Naura", description="")
    artist9 = Artist(name="Modern Jazz Quartet", description="")
    artist10 = Artist(name="Ryo Fukui", description="")

    # albums
    moonSafari = Album(artist_id=1, title="Moon Safari", description="Air's 1998 debut album Moon Safari is an influential masterpiece that not only started the international career of Jean-Benoît Dunckel and Nicolas Godin, but also found a loyal fanbase all over the world.")
    cowboyBebop = Album(artist_id=2, title="Cowboy Bebop", description="Cowboy Bebop is the first album created for the series, and the most easily categorized in terms of genre, as an outlet for many of the trademark bebop tracks. It begins with the show's theme song, \"Tank!\". The track \"Bad Dog No Biscuits\" opens with a cover of the Tom Waits composition \"Midtown\" before diverting in its interpretation.")

    #songs
    cowboyBebopSongs = [
        Song(album_id=2, title="", url="", cover=""),
        Song(album_id=2, title="", url="", cover=""),
        Song(album_id=2, title="", url="", cover=""),
        Song(album_id=2, title="", url="", cover=""),
        Song(album_id=2, title="", url="", cover=""),
        Song(album_id=2, title="", url="", cover=""),
        Song(album_id=2, title="", url="", cover=""),
        Song(album_id=2, title="", url="", cover=""),
        Song(album_id=2, title="", url="", cover=""),
        Song(album_id=2, title="", url="", cover=""),
        Song(album_id=2, title="", url="", cover=""),
    ]
    for song in cowboyBebopSongs:
        db.session.add(song)

    # Comitting
    db.session.add(artist1)
    db.session.add(artist2)
    db.session.add(artist3)
    db.session.add(artist4)
    db.session.add(artist5)
    db.session.add(artist6)
    db.session.add(artist7)
    db.session.add(artist8)
    db.session.add(artist9)
    db.session.add(artist10)

    db.session.commit()
