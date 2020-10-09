import media           # for movie class
import fresh_tomatoes  # for the HTML Udacity course website


# Here, all the movies are created with calling the Movie class from media.py
avatar = media.Movie(
    "Avatar",
    "Avatar",
    "http://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY"
    )

casino_royale = media.Movie(
    "Casino Royale",
    "James Bond: 007",
    "http://www.gstatic.com/tv/thumb/movieposters/159167/p159167_p_v8_aa.jpg",
    "https://www.youtube.com/watch?v=36mnx8dBbGE"
    )

hurt_locker = media.Movie(
    "The Hurt Locker",
    "The Hurt Locker",
    "http://www.gstatic.com/tv/thumb/movieposters/197175/p197175_p_v8_ah.jpg",
    "https://www.youtube.com/watch?v=AIbFvqFYRT4"
    )

quantum_of_solace = media.Movie(
    "Quantum of Solace",
    "James Bond: 007",
    "http://www.gstatic.com/tv/thumb/movieposters/170973/p170973_p_v8_ah.jpg",
    "https://www.youtube.com/watch?v=f6acw690AqQ"
    )

blood_diamond = media.Movie(
    "Blood Diamond",
    "Blood Diamond",
    "http://www.gstatic.com/tv/thumb/movieposters/162986/p162986_p_v8_ab.jpg",
    "https://www.youtube.com/watch?v=yknIZsvQjG4"
    )

terminator_2 = media.Movie(
    "Terminator 2: Judgement Day",
    "Terminator",
    "http://t1.gstatic.com/images?q=tbn:ANd9GcS5J6Ay6y1UT7WAI4U7Zm2KDYITrvfOI3vmaCNdGhx_0jmWiI1d",
    "https://www.youtube.com/watch?v=VVZQ39i5G1s"
    )

top_gun = media.Movie(
    "Top Gun",
    "Top Gun",
    "http://t2.gstatic.com/images?q=tbn:ANd9GcSVCaXEcuVO3eMn2X0c0_TGdISkfQMfyy1lRkTZ88sfIIj-g-5d",
    "https://www.youtube.com/watch?v=qAfbp3YX9F0"
    )

god_father = media.Movie(
    "God Father",
    "God Father",
    "http://3.bp.blogspot.com/-rj68Bw1uQJ4/TzQ9P3yaSiI/AAAAAAAAB0E/nj1kVB09M8A/s1600/godfather_ver1.jpg",
    "https://www.youtube.com/watch?v=sY1S34973zA"
    )

titanic = media.Movie(
    "Titanic",
    "Titanic",
    "https://i.ytimg.com/vi/jIhicnTgArM/movieposter.jpg",
    "https://www.youtube.com/watch?v=zCy5WQ9S4c0"
    )

# Now, all the moves are grouped into a list
movies = [
    avatar,
    casino_royale,
    hurt_locker,
    quantum_of_solace,
    blood_diamond,
    terminator_2,
    top_gun,
    god_father,
    titanic
    ]

# This function is called from the Udacity course material
#   to create the website.
# All movies (list) are sent to that function.
fresh_tomatoes.open_movies_page(movies)
