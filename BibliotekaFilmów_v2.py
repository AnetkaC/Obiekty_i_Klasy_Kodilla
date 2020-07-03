from typing import Dict, Union

from tmdbv3api import TMDb, TV, Movie

tmdb = TMDb()
tmdb.api_key = ''

movie = Movie()
tv = TV()


class Movie:

    def __init__(self, title: str, issue_year: int, movie_type: str, overview: int) -> str:
        self.title = title
        self.issue_year = issue_year
        self.movie_type = movie_type
        self.overview = overview
        self.play = 0

    def __str__(self) -> str:
        return f"{self.title} {self.issue_year}, {self.movie_type}, {self.overview}"

    def __repr__(self) -> str:
        return f"Movie(title={self.title} issue_year={self.issue_year},movie_type={self.movie_type}, views_no={self.overview})"

    def play(self) -> str:  # zwiększenie liczby odtworzeń filmu pkt 3
        self.overview += 1
        return f'Liczba wyświetleń filmu:{self.overview}'

# Pkt 7 filtruje i zwraca tylko filmy
    def get_movie(self) -> str:
        print(f'Film: {self.title}, został wyprodukowany w roku:  {self.issue_year} gatunek filmu to: {self.movie_type}, był odtworzony {self.overview} liczbę razy')



def main():
    # tworzymy obiekty klasy Movie
    title1 = Movie("Tytuł_1", 2000, "drama", 500)
    title2 = Movie("Tytuł_2", 2001, "comedy", 600)
    title3 = Movie("Tytuł_3", 2002, "drama", 700)
    title4 = Movie("Tytuł_4", 2003, "comedy", 800)
    title5 = Movie("Tytuł_5", 2004, "comedy", 900)

    print('-' * 100)
    print("pkt. 1")

# wywołujemy metodę get_movie() na każdym z nich
    title1.get_movie()
    title2.get_movie()
    title3.get_movie()
    title4.get_movie()
    title5.get_movie()

if __name__ == "__main__":
        main()

print('-' * 100)
data_movies = [
    {'title': "Tytuł 1", 'issue_year': 2000, 'movie_type': "drama", 'overview': 500},
    {'title': "Tytuł 2", 'issue_year': 2001, 'movie_type': "comedy", 'overview': 600},
    {'title': "Tytuł 3", 'issue_year': 2002, 'movie_type': "drama", 'overview': 700},
    {'title': "Tytuł 4", 'issue_year': 2003, 'movie_type': "comedy", 'overview': 800},
    {'title': "Tytuł 5", 'issue_year': 2004, 'movie_type': "comedy", 'overview': 900}
]
print("Pkt. 5 po wyświetleniu filmu jako stringa widoczny jest tytuł i rok wydania")
for row in data_movies:
    print('Film: %s, został wydany w roku %d' % (row['title'], row['issue_year']))