import pytest
from sorting.comparisons.comparison_sort import sort_movies_by_most_recent_year, sort_movies_alphabetically_by_title

# Sample movie data
@pytest.fixture
def movies():
    return [
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

@pytest.mark.test
def test_sort_by_most_recent_year(movies):
    sorted_movies = sort_movies_by_most_recent_year(movies)
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
    assert sorted_movies == expected_output

@pytest.mark.test
def test_sort_alphabetically_by_title(movies):
    sorted_movies = sort_movies_alphabetically_by_title(movies)
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
    assert sorted_movies == expected_output
