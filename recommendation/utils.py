#! /usr/bin/python
'''
@author: mahsan
'''

import ast
import getopt
import os
import sys


try:
    import simplejson as json
except ImportError:
    import json


def load_json(file_path=None):
    """
    Takes json filename as an input and returns data on valid file
    """

    if file_path is None:
        return False

    movies_data = None
    try:
        with open(file_path, "rb+") as movies_file:
            movies_data = json.load(movies_file)
    except IOError:
        raise Exception("File path is not correct.")

    return movies_data


def usage():
    """
    Print the usage of command line in case of wrong parameters
    """
    print '\nUsage: recommendation < input_movies > < file_path > [count]\n'
    print '  Example:\n'
    print '\t recommendation [1,8,9,25,45] C:\path_to_file\movies.json 10\n'


def validate_args(args):
    """
    Return dict. if command line arguments are valid, return false if not.
    """
    correct_params = True
    params = {}

    try:
        params["input_movies"] = ast.literal_eval(args[0])
    except:
        correct_params = False

    if os.path.isfile(args[1]):
        params["file_path"] = args[1]
    else:
        correct_params = False

    if len(args) == 3:
        params["show_count"] = int(args[2])
    else:
        params["show_count"] = 5

    return params if correct_params else False


def parse_args(argv):
    """
    Take the command line argument and parse it get the required parameters.
    """
    try:
        opts, args = getopt.getopt(argv, "h", ["help"])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    # check if arguments are not in actual number
    if len(args) < 2 or len(args) > 3:
        usage()
        sys.exit()

    for opt, arg in opts:
        if opt == '-h':
            usage()
            sys.exit()

    # check if arguments are valid
    params = validate_args(args)

    if params:
        return params
    else:
        usage()
        sys.exit()


def show_remommend_movies(movies, movies_dict):
    """
    Takes top recommended movies and all movies dict as an input
    and print the movie id with their name on console.
    """
    if len(movies) == 0 or not movies_dict:
        return False

    print "\n****************************************************************"
    print "\n\t\t Top Movies \n"

    for movie in movies:
        try:
            print "\t%d   -   %s" % (movie, movies_dict.get(str(movie)))
        except KeyError:
            continue
    if not movies:
        print "\t\tNo movie found\n"

    print "\n****************************************************************"
