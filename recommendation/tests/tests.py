#! /usr/bin/python
'''
@author: mahsan
'''

import os
import unittest

from recommendation.recommendation import Recommendation
from utils import load_json, validate_args


class Test(unittest.TestCase):

    def setUp(self):
        self.input_movies = [4, 7, 9, 14, 45]
        self.file_path = "data\movies.json"
        self.recommend = Recommendation(self.input_movies, self.file_path, 3)

    def tearDown(self):
        pass

    def test_load_json(self):
        # check if file valid exists
        file_data = load_json(self.file_path)
        # load_json will return dict on success
        self.assertIsInstance(file_data, dict)

    def test_movies_data(self):
        # get the the movies records from file
        movies_dict = self.recommend.get_movies_dict()
        self.assertNotIsInstance(movies_dict, list)
        self.assertDictContainsSubset({"4": "Richard III (1995)"}, movies_dict)

    def test_users_data(self):
        # get the user records from json file
        users_data = self.recommend.get_user_list()
        self.assertIsInstance(users_data, list)
        self.assertLessEqual([], users_data)

    def test_input_parameters(self):
        wrong_params = ["[12, ds, 45, 59]", "movies.json"]
        correct_params = ["23, 36, 49", "data\movies.json"]
        # check with wring parameters first
        self.assertEqual(validate_args(wrong_params), False)
        # see if parameters are valid
        self.assertDictContainsSubset({"input_movies": (23, 36, 49)},
                                      validate_args(correct_params))

    def test_recommeded_movies(self):
        # get the top matched recommended movies
        movies = self.recommend.get_recommended_movies()
        self.assertListEqual(movies, [60, 59, 30])
        self.assertEqual(len(movies), 3, "Recommended movies count is not \
                         correct")


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.test_load_json']
    unittest.main()
