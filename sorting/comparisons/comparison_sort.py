def sort_movies_by_most_recent_year(movies):
    return sorted(movies)

def sort_movies_alphabetically_by_title(movies):
    articles = ["A ", "An ", "The "]

    def remove_leading_articles(title):
        for article in articles:
            if title.startswith(article):
                return title[len(article):]
        return title

    return sorted(movies, key=lambda x: remove_leading_articles(x['title']))

