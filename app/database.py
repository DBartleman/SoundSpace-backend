from app.models import User, Artist, Album, Song, Favorite
from app import app, db
from dotenv import load_dotenv
load_dotenv()

with app.app_context():
    db.drop_all()
    db.create_all()

    user = User(email="demo@email.com", username="demo", password="demo")

    artist1 = Artist(
        name="Air", description="Air are a French music duo from Versailles, consisting of Nicolas Godin and Jean-Benoît Dunckel.")
    artist2 = Artist(name="", description="")
    artist3 = Artist(name="", description="")
    artist4 = Artist(name="", description="")
    artist5 = Artist(name="", description="")
    artist6 = Artist(name="", description="")
    artist7 = Artist(name="", description="")
    artist8 = Artist(name="", description="")
    artist9 = Artist(name="", description="")
    artist10 = Artist(name="", description="")
    artist11 = Artist(name="", description="")
    artist12 = Artist(name="", description="")
    artist13 = Artist(name="", description="")

    album1 = Album(title="Moon Safari", description="Air's 1998 debut album Moon Safari is an influential masterpiece that not only started the international career of Jean-Benoît Dunckel and Nicolas Godin, but also found a loyal fanbase all over the world.")

    deck = Deck(title="Python", user_id=1, description="")
    deck2 = Deck(title="Algorithms", user_id=1, description="")
    cards = [
        Card(deck_id=1, question="1 + 1", answer="2"),
        Card(deck_id=1, question="2 + 2", answer=" 4"),
        Card(deck_id=1, question="3 + 3", answer="6"),
        Card(deck_id=1, question="4 + 4", answer="8"),
    ]

    for card in cards:
        db.session.add(card)

    db.session.add(user)
    db.session.add(deck)
    db.session.add(deck2)

    db.session.commit()
