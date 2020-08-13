from app.models import User, Artist, Album, Song, Favorite
from app import app, db
from dotenv import load_dotenv
load_dotenv()

with app.app_context():

    # reset database
    db.drop_all()
    db.create_all()
    
    # Demo user
    user = User(email="demo@email.com", username="demo", password="demo")

    # artists
    artist1 = Artist(
        name="Air", 
        description="Air are a French music duo from Versailles, consisting of Nicolas Godin and Jean-Benoît Dunckel. After making several remixes for other acts in the first half of the 1990s, the duo released their first album, Moon Safari, in 1998. The album received universal acclaim and became an international success.")
    artist2 = Artist(
        name="The Seatbelts",             
        description="Seatbelts is a Japanese band led by composer and instrumentalist Yoko Kanno. An international ensemble comprising both a stable lineup of musicians and various collaborators, the band was assembled by Kanno in 1998 to perform the soundtrack music for the Cowboy Bebop anime series.")
    artist3 = Artist(
        name="Fred Hersch", 
        description="Fred Hersch is an American jazz pianist and educator. He has performed solo and led his own groups, including the Pocket Orchestra consisting of piano, trumpet, voice, and percussion. He was the first person to play weeklong engagements as a solo pianist at the Village Vanguard in New York City.")
    artist4 = Artist(
        name="Gregory Privat",
        description="Grégory Privat is a French piano player born in Martinique. After ten years of classical piano training, Privat started composing and improvising.")
    artist5 = Artist(
        name="Jim Lang", 
        description="James Volker Langknecht, better known as Jim Lang, is an American composer. He is known for scoring the Nickelodeon series Hey Arnold!, as well as it's feature film and television film.")
    artist6 = Artist(
        name="Kat Epple and Bob Stohl",
        description="Kat Epple and Bob Stohl were a Florida-based musical duo, who composed and recorded New Age and electronica music. They were known for innovative synthesizer orchestration and created a unique blend of \"electronic space music\" and acoustic instruments.")
    artist7 = Artist(
        name="Jerry Martin and Marc Russo", 
        description="Jerry Martin is an American music composer. He was the Lead Composer and Studio Audio Director for The Sims, and composed much of the music found in those games. Marc Russo is an American music composer and saxophonist. He began a musical career in the late 1970s, ultimately becoming a part of the contemporary jazz group Yellowjackets. Russo left the group in the 1990s, choosing to work on commercial projects, including the composition of several tracks for The Sims and its expansions.")
    artist8 = Artist(
        name="Michael Naura", 
        description="Michael Naura was a German jazz pianist, jazz editor, publicist and producer of the NDR jazz workshop. After starting out as a jazz musician, he popularized jazz as a jazz editor on the NDR radio and as a publicist.")
    artist9 = Artist(
        name="Modern Jazz Quartet", 
        description="The Modern Jazz Quartet was a jazz combo that played music influenced by classical, cool jazz, blues and bebop. For most of its history, the Quartet consisted of John Lewis (piano), Milt Jackson (vibraphone), Percy Heath (double bass), and Connie Kay (drums). The group grew out of the rhythm section of Dizzy Gillespie's big band.")
    artist10 = Artist(
        name="Ryo Fukui", 
        description="Ryo Fukui was a Japanese jazz pianist based in Sapporo. He played regularly at the \"Slowboat\" jazz club in Sapporo, which he and his wife Yasuko owned. Fukui taught and performed internationally. His work has seen a spike in popularity after his death, with several reissues of his albums.")

    # albums
    moonSafari = Album(artist_id=1, title="Moon Safari", description="Air's 1998 debut album Moon Safari is an influential masterpiece that not only started the international career of Jean-Benoît Dunckel and Nicolas Godin, but also found a loyal fanbase all over the world.")
    cowboyBebop = Album(artist_id=2, title="Cowboy Bebop", description="Cowboy Bebop is the first album created for the series, and the most easily categorized in terms of genre, as an outlet for many of the trademark bebop tracks. It begins with the show's theme song, \"Tank!\". The track \"Bad Dog No Biscuits\" opens with a cover of the Tom Waits composition \"Midtown\" before diverting in its interpretation.")
    aloneVanguard = Album(artist_id=3, title="", description="")
    kiKote = Album(artist_id=4, title="", description="")
    heyArnold = Album(artist_id=5, title="", description="")
    stellarWanderer = Album(artist_id=6, title="", description="")
    theSims = Album(artist_id=7, title="", description="")
    call = Album(artist_id=8, title="", description="")
    django = Album(artist_id=9, title="", description="")
    scenery = Album(artist_id=10, title="", description="")


    #songs
    airSongs = [
        Song(
            album_id=2,
            title="La femme dargent",
            url="music/air/01_La_femme_dargent.mp3",
            cover="music/air/cover.jpeg"),
        Song(
            album_id=2,
            title="Sexy boy",
            url="music/air/02_Sexy_boy.mp3",
            cover="music/air/cover.jpeg"),
        Song(
            album_id=2,
            title="All I need",
            url="music/air/03_All_I_need.mp3",
            cover="music/air/cover.jpeg"),
        Song(
            album_id=2,
            title="Kelly watch the stars",
            url="music/air/04_Kelly_watch_the_stars.mp3",
            cover="music/air/cover.jpeg"),
        Song(
            album_id=2,
            title="Talisman",
            url="music/air/05_Talisman.mp3",
            cover="music/air/cover.jpeg"),
        Song(
            album_id=2,
            title="Remember",
            url="music/air/06_Remember.mp3",
            cover="music/air/cover.jpeg"),
        Song(
            album_id=2,
            title="You make it easy",
            url="music/air/07_You_make_it_easy.mp3",
            cover="music/air/cover.jpeg"),
        Song(
            album_id=2,
            title="Ce matin la",
            url="music/air/08_Ce_matin_la.mp3",
            cover="music/air/cover.jpeg"),
        Song(
            album_id=2,
            title="New star in the sky",
            url="music/air/09_New_star_in_the_sky.mp3",
            cover="music/air/cover.jpeg"),
        Song(
            album_id=2,
            title="Le voyage de Penelope",
            url="music/air/10_Le_voyage_de_Penelope.mp3",
            cover="music/air/cover.jpeg"),
    ]

    cowboyBebopSongs = [
        Song(
            album_id=2, 
            title="Tank", 
            url="music/cb/01_Tank.mp3", 
            cover="music/cb/cover.jpeg"),
        Song(
            album_id=2, 
            title="Rush", 
            url="music/cb/02_Rush.mp3", 
            cover="music/cb/cover.jpeg"),
        Song(
            album_id=2, 
            title="Spokey Dokey",
            url="music/cb/03_Spokey_Dokey.mp3", 
            cover="music/cb/cover.jpeg"),
        Song(
            album_id=2, 
            title="Bad Dog No Biscuits", 
            url="music/cb/04_Bad_Dog_No_Biscuits.mp3", 
            cover="music/cb/cover.jpeg"),
        Song(
            album_id=2, 
            title="Cat Blues", 
            url="music/cb/05_Cat_Blues.mp3", 
            cover="music/cb/cover.jpeg"),
        Song(
            album_id=2, 
            title="Cosmos", 
            url="music/cb/06_Cosmos.mp3", 
            cover="music/cb/cover.jpeg"),
        Song(
            album_id=2, 
            title="Space Lion", 
            url="music/cb/07_Space_Lion.mp3", 
            cover="music/cb/cover.jpeg"),
        Song(
            album_id=2, 
            title="Waltz for Zizi", 
            url="music/cb/08_Waltz_for_Zizi.mp3", 
            cover="music/cb/cover.jpeg"),
        Song(
            album_id=2, 
            title="Piano Black", 
            url="music/cb/09_Piano_Black.mp3", 
            cover="music/cb/cover.jpeg"),
        Song(
            album_id=2, 
            title="Pot City", 
            url="music/cb/10_Pot_City.mp3",
            cover="music/cb/cover.jpeg"),
        Song(
            album_id=2,
            title="Too Good Too Bad",
            url="music/cb/11_Too_Good_Too_Bad.mp3",
            cover="music/cb/cover.jpeg"),
        Song(
            album_id=2,
            title="Car 24",
            url="music/cb/12_Car_24.mp3",
            cover="music/cb/cover.jpeg"),
        Song(
            album_id=2, 
            title="The Egg and I", 
            url="music/cb/13_The_Egg_and_I.mp3",
            cover="music/cb/cover.jpeg"),
        Song(
            album_id=2, 
            title="Felt Tip Pen", 
            url="music/cb/14_Felt_Tip_Pen.mp3",
            cover="music/cb/cover.jpeg"),
        Song(
            album_id=2, 
            title="Digging my Potato", 
            url="music/cb/16_Digging_my_Potato.mp3",
            cover="music/cb/cover.jpeg"),
        Song(
            album_id=2,
            title="Memory",
            url="music/cb/17_Memory.mp3",
            cover="music/cb/cover.jpeg"),
    ]

    fredSongs = [
        Song(
            album_id=3,
            title="In the wee small hours of the morning",
            url="music/fred/01_In_the_Wee_Small_Hours.mp3",
            cover="music/fred/cover.jpeg"),
        Song(
            album_id=3,
            title="Down Home",
            url="music/fred/02_Down_Home.mp3",
            cover="music/fred/cover.jpeg"),
        Song(
            album_id=3,
            title="Echoes",
            url="music/fred/03_Echoes.mp3",
            cover="music/fred/cover.jpeg"),
        Song(
            album_id=3,
            title="Lee's Dream",
            url="music/fred/04_Lees_Dream.mp3",
            cover="music/fred/cover.jpeg"),
        Song(
            album_id=3,
            title="Pastorale",
            url="music/fred/05_Pastorale.mp3",
            cover="music/fred/cover.jpeg"),
        Song(
            album_id=3,
            title="Doce de Coco",
            url="music/fred/06_Doce_de_Coco.mp3",
            cover="music/fred/cover.jpeg"),
        Song(
            album_id=3,
            title="Memories of You",
            url="music/fred/07_Memories_of_You.mp3",
            cover="music/fred/cover.jpeg"),
        Song(
            album_id=3,
            title="Work",
            url="music/fred/08_Work.mp3",
            cover="music/fred/cover.jpeg"),
        Song(
            album_id=3,
            title="Doxy",
            url="music/fred/09_Doxy.mp3",
            cover="music/fred/cover.jpeg"),
    ]

    gregSongs = [
        Song(
            album_id=4,
            title="Le Nouvel Esclave",
            url="music/greg/01_Le_Nouvel_Esclave.mp3",
            cover="music/greg/cover.jpeg"),
        Song(
            album_id=4,
            title="Mi Nou La",
            url="music/greg/02_Mi_Nou_La.mp3",
            cover="music/greg/cover.jpeg"),
        Song(
            album_id=4,
            title="Ki Kote",
            url="music/greg/03_Ki_Kote.mp3",
            cover="music/greg/cover.jpeg"),
        Song(
            album_id=4,
            title="Pa Pe",
            url="music/greg/04_Pa_Pe.mp3",
            cover="music/greg/cover.jpeg"),
        Song(
            album_id=4,
            title="An Fwedi A",
            url="music/greg/05_An_Fwedi_A.mp3",
            cover="music/greg/cover.jpeg"),
        Song(
            album_id=4,
            title="Koute Pou Tann",
            url="music/greg/06_Koute_Pou_Tann.mp3",
            cover="music/greg/cover.jpeg"),
        Song(
            album_id=4,
            title="Fos Ti Moun",
            url="music/greg/07_Fos_Ti_Moun.mp3",
            cover="music/greg/cover.jpeg"),
        Song(
            album_id=4,
            title="Kontan We Zot",
            url="music/greg/08_Kontan_We_Zot.mp3",
            cover="music/greg/cover.jpeg"),
        Song(
            album_id=4,
            title="An Piano Epi an Ka",
            url="music/greg/09_An_Piano_Epi_an_Ka.mp3",
            cover="music/greg/cover.jpeg"),
        Song(
            album_id=4,
            title="Run Away",
            url="music/greg/10_Run_Away.mp3",
            cover="music/greg/cover.jpeg"),
        Song(
            album_id=4,
            title="Signe Et Sens",
            url="music/greg/11_Signe_Et_Sens.mp3",
            cover="music/greg/cover.jpeg"),
    ]

    jimSongs = [
        Song(
            album_id=5,
            title="Hey Arnold! Theme",
            url="music/jim/01_Hey_Arnold!_Theme.m4a",
            cover="music/jim/cover.jpeg"),
        Song(
            album_id=5,
            title="Back to School Fumblerooski",
            url="music/jim/02_Back_to_School_Fumblerooski.m4a",
            cover="music/jim/cover.jpeg"),
        Song(
            album_id=5,
            title="Kick the Can (Extended Mix)",
            url="music/jim/03_Kick_the_Can_(Extended_Mix).m4a",
            cover="music/jim/cover.jpeg"),
        Song(
            album_id=5,
            title="Street Ball (Mix)",
            url="music/jim/04_Street_Ball_(Mix).m4a",
            cover="music/jim/cover.jpeg"),
        Song(
            album_id=5,
            title="Caper at Gene's",
            url="music/jim/05_Caper_at_Gene's.m4a",
            cover="music/jim/cover.jpeg"),
        Song(
            album_id=5,
            title="Headin' South",
            url="music/jim/06_Headin'_South.m4a",
            cover="music/jim/cover.jpeg"),
        Song(
            album_id=5,
            title="Harold's Boogie",
            url="music/jim/07_Harold's_Boogie.m4a",
            cover="music/jim/cover.jpeg"),
        Song(
            album_id=5,
            title="Hammer and Tongs",
            url="music/jim/08_Hammer_and_Tongs.m4a",
            cover="music/jim/cover.jpeg"),
        Song(
            album_id=5,
            title="Helga's True Love",
            url="music/jim/09_Helga's_True_Love.m4a",
            cover="music/jim/cover.jpeg"),
        Song(
            album_id=5,
            title="Home Wit Jerome",
            url="music/jim/10_Home_Wit_Jerome.m4a",
            cover="music/jim/cover.jpeg"),
        Song(
            album_id=5,
            title="Alternate Ending Theme (Hammond)",
            url="music/jim/11_Alternate_Ending_Theme_(Hammond).m4a",
            cover="music/jim/cover.jpeg"),
        Song(
            album_id=5,
            title="That's Wack",
            url="music/jim/12_That's_Wack.m4a",
            cover="music/jim/cover.jpeg"),
        Song(
            album_id=5,
            title="Invisible Hippo (Nick)",
            url="music/jim/13_Invisible_Hippo_(Nick).m4a",
            cover="music/jim/cover.jpeg"),
        Song(
            album_id=5,
            title="Groove Remote (Abner Lowjack)",
            url="music/jim/14_Groove_Remote_(Abner_Lowjack)_[Mi.m4a",
            cover="music/jim/cover.jpeg"),
        Song(
            album_id=5,
            title="Invisible Hippo",
            url="music/jim/15_Invisible_Hippo.m4a",
            cover="music/jim/cover.jpeg"),
        Song(
            album_id=5,
            title="Groove Remote",
            url="music/jim/16_Groove_Remote.m4a",
            cover="music/jim/cover.jpeg"),
        Song(
            album_id=5,
            title="Christmas Ending Theme",
            url="music/jim/17_Christmas_Ending_Theme.m4a",
            cover="music/jim/cover.jpeg"),
        Song(
            album_id=5,
            title="The Moral Is... A Real Scorcher",
            url="music/jim/18_The_Moral_Is__A_Real_Scorcher.m4a",
            cover="music/jim/cover.jpeg"),
        Song(
            album_id=5,
            title="Meet Angel",
            url="music/jim/19_Meet_Angel.m4a",
            cover="music/jim/cover.jpeg"),
        Song(
            album_id=5,
            title="Alternate Ending Theme (Version 2)",
            url="music/jim/20_Alternate_Ending_Theme_(Version_2.m4a",
            cover="music/jim/cover.jpeg"),
        Song(
            album_id=5,
            title="Thinkin' It Over",
            url="music/jim/21_Thinkin'_It_Over.m4a",
            cover="music/jim/cover.jpeg"),
        Song(
            album_id=5,
            title="Sid & Stink",
            url="music/jim/22_Sid_&_Stink.m4a",
            cover="music/jim/cover.jpeg"),
        Song(
            album_id=5,
            title="Pigeon Man Ending Theme",
            url="music/jim/23_Pigeon_Man_Ending_Theme.m4a",
            cover="music/jim/cover.jpeg"),
        Song(
            album_id=5,
            title="Alternate Ending Theme (Version 3)",
            url="music/jim/24_Alternate_Ending_Theme_(Version_3.m4a",
            cover="music/jim/cover.jpeg"),
        Song(
            album_id=5,
            title="Mom and Dad",
            url="music/jim/25_Mom_and_Dad.m4a",
            cover="music/jim/cover.jpeg"),
        Song(
            album_id=5,
            title="Parent's Dat Ending Theme",
            url="music/jim/26_Parents_Day_Ending_Theme.m4a",
            cover="music/jim/cover.jpeg"),
        Song(
            album_id=5,
            title="The Journal",
            url="music/jim/27_The_Journal.m4a",
            cover="music/jim/cover.jpeg"),
        Song(
            album_id=5,
            title="Ending Theme",
            url="music/jim/28_Ending_Theme.m4a",
            cover="music/jim/cover.jpeg"),
        Song(
            album_id=5,
            title="Hey Arnold! Theme (20th Anniversary)",
            url="music/jim/29_Hey_Arnold!_Theme_(20th_Anniversa.m4a",
            cover="music/jim/cover.jpeg"),
        Song(
            album_id=5,
            title="Stompin' (Bonus Track)",
            url="music/jim/30_Stompin'_(Bonus_Track).m4a",
            cover="music/jim/cover.jpeg"),
        Song(
            album_id=5,
            title="Stompin' (Cover)",
            url="music/jim/31_'Stompin,'_Cover.mp3",
            cover="music/jim/cover.jpeg"),
    ]

    katSongs = [
        Song(
            album_id=6,
            title="Sanctus Spiritus",
            url="music/kat/01_Sanctus_Spiritus.mp3",
            cover="music/kat/cover.jpeg"),
        Song(
            album_id=6,
            title="Stellar Wanderer",
            url="music/kat/02_Stellar_Wanderer.mp3",
            cover="music/kat/cover.jpeg"),
        Song(
            album_id=6,
            title="Titanium Cave",
            url="music/kat/03_Titanium_Cave.mp3",
            cover="music/kat/cover.jpeg"),
        Song(
            album_id=6,
            title="Nine Unknown Men",
            url="music/kat/04_Nine_Unknown_Men.mp3",
            cover="music/kat/cover.jpeg"),
        Song(
            album_id=6,
            title="Beyond The Towers",
            url="music/kat/05_Beyond_The_Towers.mp3",
            cover="music/kat/cover.jpeg"),
    ]

    maxSongs = [
        Song(
            album_id=7,
            title="Building Mode 1",
            url="music/max/01_Building_Mode_1.mp3",
            cover="music/max/cover.jpeg"),
        Song(
            album_id=7,
            title="Building Mode 2",
            url="music/max/01_Building_Mode_2.mp3",
            cover="music/max/cover.jpeg"),
        Song(
            album_id=7,
            title="Building Mode 3",
            url="music/max/01_Building_Mode_3.mp3",
            cover="music/max/cover.jpeg"),
        Song(
            album_id=7,
            title="Building Mode 4",
            url="music/max/01_Building_Mode_4.mp3",
            cover="music/max/cover.jpeg"),
        Song(
            album_id=7,
            title="Building Mode 5",
            url="music/max/01_Building_Mode_5.mp3",
            cover="music/max/cover.jpeg"),
        Song(
            album_id=7,
            title="Buy Mode 1",
            url="music/max/01_Buy_Mode_1.mp3",
            cover="music/max/cover.jpeg"),
        Song(
            album_id=7,
            title="Buy Mode 2",
            url="music/max/01_Buy_Mode_2.mp3",
            cover="music/max/cover.jpeg"),
        Song(
            album_id=7,
            title="Buy Mode 3",
            url="music/max/01_Buy_Mode_3.mp3",
            cover="music/max/cover.jpeg"),
        Song(
            album_id=7,
            title="Neighborhood 1",
            url="music/max/01_Neighborhood_1.mp3",
            cover="music/max/cover.jpeg"),
        Song(
            album_id=7,
            title="Neighborhood 2",
            url="music/max/01_Neighborhood_2.mp3",
            cover="music/max/cover.jpeg"),
        Song(
            album_id=7,
            title="Neighborhood 3",
            url="music/max/01_Neighborhood_3.mp3",
            cover="music/max/cover.jpeg"),
        Song(
            album_id=7,
            title="",
            url="",
            cover="music/max/cover.jpeg"),
    ]

    micSongs = [
        
    ]

    for song in airSongs:
        db.session.add(song)
    for song in cowboyBebopSongs:
        db.session.add(song)
    for song in fredSongs:
        db.session.add(song)
    for song in gregSongs:
        db.session.add(song)
    for song in jimSongs:
        db.session.add(song)
    for song in katSongs:
        db.session.add(song)
    for song in maxSongs:
        db.session.add(song)
    for song in :
        db.session.add(song)
    for song in :
        db.session.add(song)
    for song in :
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
