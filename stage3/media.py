import webbrowser


# define object
class Movie():
    def __init__(self, movie_title, movie_storyline, movie_director, movie_release_date, poster_image,
                 trailer_youtube):
        '''

        :param movie_title: movie title
        :param movie_storyline: storyline
        :param movie_director: director name
        :param movie_release_date: release date
        :param poster_image: poster image url
        :param trailer_youtube: trailer url
        '''
        self.title = movie_title
        self.storyline = movie_storyline
        self.director = movie_director
        self.release_date = movie_release_date
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        '''

        :return: nothing but showing the youtube trailer on the web page
        '''
        webbrowser.open(self.trailer_youtube_url)
