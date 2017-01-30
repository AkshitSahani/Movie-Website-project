import webbrowser

class Movie():
    '''This is a class called Movie. It is used to store a number of features for each of its instances.'''

    def __init__(self, movie_title, movie_storyline, movie_release_date, poster_image, trailer_youtube):
        '''This function creates space in memory for the class (Movie in this case) and its attributes.''' 
        self.title = movie_title
        self.storyline = movie_storyline
        self.release_date = movie_release_date
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        '''This function will play the trailer for the instances of the class. It will open a web browser and go
to the youtube url for each instance'''
        webbrowser.open(self.trailer_youtube_url)
        
