import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)  # send request for data
website = response.text

soap = BeautifulSoup(website, "html.parser")  # create parser
movie_tags = soap.find_all(name="h3", class_="title")  # get all the movie name tags from website
movie_names = [names.getText() for names in movie_tags]  # get movie names from tags
# list starts with 100th place, we need to reverse that
top_movies = movie_names[::-1]

# save movie list in .txt file
with open("top_movies.txt", mode="w") as file:
	for movie in top_movies:
		if "85)" in movie:  # 85th movie name had wrong encoding
			continue
		file.write(f"{movie}\n")
