import media

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
        "https://en.wikipedia.org/wiki/File:Gladiator_ver1.jpg",
        "https://www.youtube.com/watch?v=IvTT29cavKo")

gladiator.show_trailer()
