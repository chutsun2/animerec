import requests 
from bs4 import BeautifulSoup

URL = "https://myanimelist.net/anime.php"
r = requests.get(URL).text

soup = BeautifulSoup(r,'lxml')
page = soup.find_all('div', class_ = "genre-link")
studios = page[-3].find_all('div',class_ = "genre-list al")
for studio in studios:
    print(studio.a.prettify())



