"""
Biblioteka filmów zad. 2
"""

import random #generator liczb losowych
from datetime import date


class Movie:
    def __init__(self, title: str, year: int, genre: int) -> str:
        self.title = title
        self.year = year
        self.genre = genre

        # Variables
        self.views = 0

    def __str__(self)-> str:
        return f"{self.title} ({self.year})"

    def play(self)-> str: #zwiększamy liczbę odtworzeń o 1
        self.views += 1
        return print(self)


class Series(Movie):
    def __init__(self, season: int, episode: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.season = season
        self.episode = episode

    def __str__(self):
        return f"{self.title} - {self.season}{self.episode}"


class Filmoteka:
    def __init__(self):
        self.movie_database = [
            Movie(title="Movie 1", year="1994", genre="drama"),
            Movie(title="Movie 2", year="1972", genre="gangster"),
            Movie(title="Movie 3", year="2012", genre="documentary"),
            Movie(title="Movie 4", year="2001", genre="comedy"),
            Movie(title="Movie 5", year="1994", genre="drama"),
            Movie(title="Movie 6", year="2002", genre="comedy"),
            Movie(title="Movie 7", year="2005", genre="animated"),
            Series(title="Series 1", year="2011", genre="fantasy", season="S01", episode="E01"),
            Series(title="Series 2", year="2011", genre="fantasy", season="S01", episode="E02"),
            Series(title="Series 3", year="2011", genre="fantasy", season="S01", episode="E03"),
            Series(title="Series 4", year="2011", genre="fantasy", season="S02", episode="E01"),
            Series(title="Series 5", year="1994", genre="comedy", season="S01", episode="E01"),
            Series(title="Series 6", year="1994", genre="comedy", season="S01", episode="E02"),
            Series(title="Series 7", year="1994", genre="comedy", season="S02", episode="E01"),
            Series(title="Series 8", year="2019", genre="fantasy", season="S01", episode="E01")
        ]

    def get_movies(self):
        self.movies_only = [item for item in self.movie_database if (isinstance(item, Movie) and not isinstance(item, Series))]
        return sorted(self.movies_only, key=lambda movie: movie.title)

    def get_series(self):
        self.series_only = [item for item in self.movie_database if isinstance(item, Series)]
        return sorted(self.series_only, key=lambda series: series.title)

    def search(self, keyword):
        for item in self.movie_database:
            if item.title == keyword:
                return item
            else:
                pass
        else:
            return "Brak filmu w bibliotece!"

    def generate_views(self):
        self.movie_database[random.randint(0, len(self.movie_database)-1)].views += random.randint(100, 1000)
        return True

    def top_titles(self, content_type=None, top_counter=3):
        if content_type == None:
            return sorted(self.movie_database, key=lambda movie: movie.views, reverse=True)[0:top_counter]
        elif content_type == "Movie":
            self.movies_only = [item for item in self.movie_database if (isinstance(item, Movie) and not isinstance(item, Series))]
            return sorted(self.movies_only, key=lambda movie: movie.views, reverse=True)[0:top_counter]
        elif content_type == "Series":
            self.series_only = [item for item in self.movie_database if isinstance(item, Series)]
            return sorted(self.series_only, key=lambda movie: movie.views, reverse=True)[0:top_counter]
        else:
            return 0


if __name__ == "__main__":
    print("\n Biblioteka Filmów!\n")
    bfg = Filmoteka()

    print('*' * 150)

    print("Funkcja get_movies():\n") #zwraca listę filmów
    for movie in bfg.get_movies():
        print(movie.title)

    print('-' * 100)

    print("Funkcja get_series():\n") #zwraca listę seriali
    for series in bfg.get_series():
        print(f"{series.title} {series.season}{series.episode}")
    print('-' * 100)

    print("Funkcja search(Movie) - (TRUE):\n")
    print(bfg.search("Movie 1"))


    print("Funkcja search(Movie) - (FALSE):\n")
    print(bfg.search("Avatar"))
    print('-' * 100)

    print("Funkcja generate_views():\n")
    for i in range(10):
        bfg.generate_views()
    print('-' * 100)


    print("Funkcja top_titles():\n")
    print(f"Najpopularniejsze filmy i seriale dnia {date.today()}:\n")
    for item in bfg.top_titles(content_type="Movie", top_counter=5):
        print(f"{item.title}: {item.views}")
    print('-' * 100)
