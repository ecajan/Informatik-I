#!/usr/bin/env python3

# The purpose of this file is illustrating the class usages. This script
# is irrelevant for the grading and you can freely change its contents.

from task.movie import Movie
from task.moviebox import MovieBox
from task.library import Library

a = Movie("The Shawshank Redemption", ["Robbins", "Freeman"], 142)
b = Movie("The Godfather", ["Brando", "Pacino"], 175)
c = Movie("12 Angry Men", ["Fonda", "Cobb"], 96)
d = MovieBox("Top Movies", [b, c])

l = Library()
l.add_movie(a)
l.add_movie(d)
print(l.get_movies())
print(l.get_total_duration())

####################################### library #######################################

#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from task.movie import Movie
from task.moviebox import MovieBox

class Library:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        if isinstance(movie, Movie):
            if movie not in self.movies:
                self.movies.append(movie)
        elif isinstance(movie, MovieBox):
            for m in movie.get_movies():
                if m not in self.movies:
                    self.movies.append(m)

    def get_movies(self):
        all_movies = []
        for m in self.movies:
            if isinstance(m, MovieBox):
                all_movies.extend(m.get_movies())
            else:
                all_movies.append(m)
        return sorted(set(all_movies), key=lambda x: x.get_title())

    def get_total_duration(self):
        return sum(m.get_duration() for m in self.movies if isinstance(m, Movie))


####################################### movie #######################################

#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

class Movie:

    def __init__(self, title, actors, duration):

        if not title or not actors or duration < 1:
            raise Warning("invalid movie")
        self.title = title
        self.actors = actors
        self.duration = duration

    def get_title(self):

        return self.title

    def get_actors(self):

        return self.actors

    def get_duration(self):

        return self.duration
    
    def __repr__(self):

        return f'Movie("{self.title}", {self.actors}, {self.duration})'
    
    def __eq__(self, other):

        if isinstance(other, Movie):
            return (self.title == other.title and self.actors == other.actors and self.duration == other.duration)
        return False
    
    def __hash__(self):

        return hash((self.title, tuple(self.actors), self.duration))


####################################### moviebox #######################################

#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from task.movie import Movie


class MovieBox:
    def __init__(self, title, movies):
        if not title or not movies or any(not isinstance(movie, Movie) for movie in movies):
            raise Warning("invalid moviebox")
        self.title = title
        self.movies = movies

    def get_title(self):
        
        return self.title

    def get_actors(self):
        
        actorbox = []
        for movie in self.movies:
            if Movie.actor not in actorbox:
                actorbox.append(Movie.actor)
        return sorted(actorbox)

    def get_duration(self):
        
        return sum(movie.get_duration() for movie in self.movies)

    def get_movies(self):
        
        return self.movies

    def __eq__(self, other):

        if isinstance(other, MovieBox):
            return self.title == other.title and self.movies == other.movies
        return False

    def __hash__(self):

        return hash((self.title, tuple(self.movies)))