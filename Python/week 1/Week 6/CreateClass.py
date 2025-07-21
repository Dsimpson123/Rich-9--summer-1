# Create a class to represent a video game or movie collection
#Create a constutor method _init__
#3 Create a list for the video games and movies each
#4 Create a instance variable for the users favorite movie and video game
#5 Create the following functions for your class
#6 A function to display all of the video games




class Collection:
    def __init__(self, movieList=None, gameList=None):
        self.movielist = movieList if movieList is not None else []
        self.gamelist = gameList if gameList is not None else []
        self.favGame = None
        self.favMovie = None


    def display_movies(self,):
        for movie in self.movielist:
            print(movie)

    def display_games(self):
        for game in self.gamelist:
            print(game)

    def add_movie(self, movie):
        self.movielist.append(movie)

    def add_game(self, game):
        self.gamelist.append(game)

    def remove_movie(self, movie):
        if movie in self.movielist:
            self.movielist.remove(movie)
        else:
            print(f"Movie '{movie}' not found.")

    def remove_game(self, game):
        if game in self.gamelist:
            self.gamelist.remove(game)
        else:
            print(f"Game '{game}' not found.")

    def DisplayFavMovie(self, movie):
        if movie in self.movielist:
            self.favMovie = movie
        else:
            print(f"Movie '{movie}' not in collection.")

    def set_favorite_game(self, game):
        if game in self.gamelist:
            self.favGame = game
        else:
            print(f"Game '{game}' not in collection.")


    def DisplayCollection(self):
        self.DisplayGames()
        self.DisplayFavGame()
        self.DisplayMovies()
        self.DisplayFavMovie()

    def SetFavMovie(self, movie):
            if movie not in self.movielist:
                self.AddMovie(movie)
                self.favMovie = movie

    def SetFavGame(self,game):
            if game not in self.gamelist:
                self.add_game(game)
            self.FavGame = game