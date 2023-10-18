from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, "html.parser")

all_movies = [title.getText() for title in soup.find_all(name="h3", class_="title")]
all_movies.reverse()

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for movie in all_movies:
        file.write(f"{movie}\n")
