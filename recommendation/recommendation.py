#! /usr/bin/python
'''
@author: mahsan
'''
import sys
import operator

from utils import load_json, show_remommend_movies, parse_args


class Recommendation(object):
    """
    Recommendation provides similar movies recommendation to user based on
    provided list of movies and user data.

    :param input_movies: List of input movies for use to calculate
            recommended movies.
    :type input_movies: List

    :param file_path: Complete Path to a Json file, containing list of movies
            and users data.
    :type file_path: string

    :param count: Count to number of recommended movies to show in output,
            default value is 5.
    :type count: integer
    """

    def __init__(self, input_movies, file_path, count=5):
        # Call parent constructor function
        super(Recommendation, self).__init__()

        self.movies_data = load_json(file_path)
        self.input_movies = input_movies
        self.show_count = count

    def get_movies_dict(self):
        """Return the all movies dict"""
        return self.movies_data.get("movies")

    def get_user_list(self):
        """Return all users list"""
        return self.movies_data.get("users")

    def get_recommended_movies(self):
        """
        Calculate the recommended movies for user based on data and input list,
        most relevant movies will be returned.
        """
        movies_dict = self.get_movies_dict()
        users_list = self.get_user_list()

        # Get the similar movies based on score
        movies_similirity_score = self.get_similar_movies(movies_dict.keys(),
                                                          users_list)
        # sorting the dict based on score of each movie
        sorted_movies_score = sorted(movies_similirity_score.items(),
                                     key=operator.itemgetter(1), reverse=True)

        return [id for id, score in sorted_movies_score[:self.show_count]]

    def get_similar_movies(self, movies_list, users_list):
        """
        Takes both movies and user lists to get similar movies based on their
        score. Score are adding up across each input movies and higher the
        score more chance to go in recommendation movies list.

        :param movies_list: list of all movies those were watched by users
        :type movies_list: list
        :param users_list: Users list with their movies watched set
        :type users_list: list
        """
        movies_score = {}
        # loop over each input movie to compare it with movies
        for input_movie in list(set(self.input_movies)):
            # loop over all movies user watched
            for movie in movies_list:
                movie = int(movie)
                # ignore if this is input movie or input not in user
                # watched movies
                if movie == input_movie or str(input_movie) not in movies_list:
                    continue
                # getting similarity score based on formula
                score = self.get_similirity_score(input_movie, movie,
                                                  users_list)
                # adding up the score for each movie across input movies
                try:
                    # if movie already there then just add up with previous
                    # score.
                    movies_score[movie] = movies_score[movie] + score
                except KeyError:
                    # if this is new movie the add it here in dict
                    movies_score[movie] = score

        return movies_score

    def get_similirity_score(self, input_movie, other_movie, users_data):
        """
        Get the similarity score of input movie to other movie based on
        user data. Formula is to calculate the similarity:

        score = (AB / A + B -AB)

        Here AB is both movies were watched together, A is number of count
        input movie was watched and B is number of movie other movie watched.

        :param input_movie: One input movie to compare with other movie to get
                score.
        :type input_movie: integer
        :param other_movie: Second movie to which we calculate the score with
                input movie.
        :type other_movie: integer
        :param users_data: list of users with movies record
        :type users_data: list
        """
        # initilazing all with zero at start
        input_movie_count = other_movie_count = both_occurance_count = 0

        for user_set in users_data:
            user_movies = user_set.get("movies")
            # Increment if input movie is in user watched movies
            if input_movie in user_movies:
                input_movie_count += 1
            # Increment if other movie is in user watched movies
            if other_movie in user_movies:
                other_movie_count += 1
            # Increment if both input and other movie is in user watched movies
            if input_movie in user_movies and other_movie in user_movies:
                both_occurance_count += 1
        # here is formula applied on calculated number of both movies
        # to get score
        return (float(both_occurance_count) / (input_movie_count +
                other_movie_count - both_occurance_count))


def main():
    """
    main function to start the application
    """
    # parse the parameters
    params = parse_args(sys.argv[1:])
    if not params:
        return

    # create the object and pass the params required
    recommend = Recommendation(params.get("input_movies"),
                               params.get("file_path"),
                               params.get("show_count"))
    # get he recommends movies based on data provided
    top_movies = recommend.get_recommended_movies()
    # print the movies on user console
    show_remommend_movies(top_movies, recommend.get_movies_dict())

    return 0
