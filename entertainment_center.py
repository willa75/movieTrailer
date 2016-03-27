import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", 
						"A story of a boy and his toys that come to life.", 
						"http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v8_ab.jpg", 
						"https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print toy_story.storyline

sherlock = media.Movie("Sherlock Holmes",
						"Sherlock Holmes is a 2009 action mystery film based on the character of the same name created by Sir Arthur Conan Doyle.",
						"http://ia.media-imdb.com/images/M/MV5BMTg0NjEwNjUxM15BMl5BanBnXkFtZTcwMzk0MjQ5Mg@@._V1_UY1200_CR86,0,630,1200_AL_.jpg",
						"https://www.youtube.com/watch?v=Egcx63-FfTE")

movies = [toy_story, sherlock]

fresh_tomatoes.open_movies_page(movies)