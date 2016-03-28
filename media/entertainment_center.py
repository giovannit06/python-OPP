import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
        "A story of a boy and his toys that come to life",
        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print(toy_story.storyline)

avatar = media.Movie("Avatar",
        "A marine on an alien planet",
        "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
        "http://www.youtube.com/watch?v=5PSNL1qE6VY")

#print(avatar.storyline)
#avatar.show_trailer()

gladiator = media.Movie("Gladiator",
        "A general became a slave than defied the emperor",
        "https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",
        "https://www.youtube.com/watch?v=IvTT29cavKo")

#gladiator.show_trailer()

school_of_rock = media.Movie("School of Rock", "Using rock music to learn",
        "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
        "https://www.youtube.com/watch?v=3PsUJFEBC74")
ratatouille = media.Movie("Ratatouille", "A rat is a chef in Paris",
        "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
        "https://www.youtube.com/watch?v=c3sBBRxDAqk")
midnight_in_paris = media.Movie("Midnight in Paris", 
        "Going back in time to meet authors",
        "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
        "https://upload.com/watch?v=FAfR8omt-CY")

movies = [toy_story, avatar, gladiator, school_of_rock, ratatouille,
        midnight_in_paris]
fresh_tomatoes.open_movies_page(movies)
