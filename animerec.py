import requests 
from bs4 import BeautifulSoup
import csv 
import os
import time
import random

#Function that finds anime title and anime genre, organizes it, and outputs in the form of csv file 
def findanimetitle(studioURL,csvfile):
        csvwriter = csv.writer(csvfile)
        r = requests.get(studioURL).text
        studiosoup = BeautifulSoup(r,'lxml')
        animes = studiosoup.find('div',class_="js-categories-seasonal tile-anime-list js-seasonal-anime-append")
        for anime in animes.find_all('div',attrs={'data-genre': True}):
            csvwriter.writerow([anime.find('div', class_ = 'title').a.text,anime['data-genre']])
        
    
#Declaring Variables
mainURL = "https://myanimelist.net" #main website URL
URL = mainURL + "/anime/producer"
r = requests.get(URL).text #requesting URL
soup = BeautifulSoup(r,'lxml')
page = soup.find('div', class_ = "anime-manga-search ml8 mr8 pt24 pb8")
studios = page.find_all('div',class_ = "genre-list al")

#Writing CSV file
save_path = 'C:/Users/user/OneDrive/Desktop/Project/animerec'
filename = os.path.join(save_path, 'animedata.csv')
with open(filename, 'a', encoding = 'utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    fields = ['animename','genre']
    csvwriter.writerow(fields)
    for studio in studios:
        print(studio.a['href'])
        delay = random.uniform(2,5)
        time.sleep(delay)
        studioURL = mainURL + studio.a['href']
        findanimetitle(studioURL,csvfile)
    
    



