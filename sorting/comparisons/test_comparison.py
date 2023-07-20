import pytest
import sys
import os

# Add the parent directory of the tests package to the Python path
current_directory = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current_directory)
sys.path.append(parent_directory)

# Now you can import the sorting module
from sorting.comparisons.comparison_sort import sort_movies_by_most_recent_year, sort_movies_alphabetically_by_title

def test_exist():
    assert sort_movies_alphabetically_by_title()

def setUp(self):
        # Sample movie data
        self.movies = [
            {
                'title': 'The Great Gatsby',
                'year': 2013,
                'genres': ['Drama', 'Romance']
            },
            {
                'title': 'An Inconvenient Truth',
                'year': 2006,
                'genres': ['Documentary']
            },
            {
                'title': 'Memento',
                'year': 2000,
                'genres': ['Mystery', 'Thriller']
            },
            {
                'title': 'Avatar',
                'year': 2009,
                'genres': ['Action', 'Adventure', 'Fantasy']
            }
        ]

def test_sort_by_most_recent_year(self):
        sorted_movies = sort_movies_by_most_recent_year(self.movies)
        expected_output = [
            {
                'title': 'The Great Gatsby',
                'year': 2013,
                'genres': ['Drama', 'Romance']
            },
            {
                'title': 'Avatar',
                'year': 2009,
                'genres': ['Action', 'Adventure', 'Fantasy']
            },
            {
                'title': 'An Inconvenient Truth',
                'year': 2006,
                'genres': ['Documentary']
            },
            {
                'title': 'Memento',
                'year': 2000,
                'genres': ['Mystery', 'Thriller']
            }
        ]
        self.assertEqual(sorted_movies, expected_output)

def test_sort_alphabetically_by_title(self):
        sorted_movies = sort_movies_alphabetically_by_title(self.movies)
        expected_output = [
            {
                'title': 'Avatar',
                'year': 2009,
                'genres': ['Action', 'Adventure', 'Fantasy']
            },
            {
                'title': 'The Great Gatsby',
                'year': 2013,
                'genres': ['Drama', 'Romance']
            },
            {
                'title': 'Memento',
                'year': 2000,
                'genres': ['Mystery', 'Thriller']
            },
            {
                'title': 'An Inconvenient Truth',
                'year': 2006,
                'genres': ['Documentary']
            }
        ]
        self.assertEqual(sorted_movies, expected_output)
