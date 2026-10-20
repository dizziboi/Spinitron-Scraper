import requests
from bs4 import BeautifulSoup

urlIN = input("Type in a URL: ")
r= requests.get(urlIN)
#prints status code
print("Status Code: ",r)

#parsing the site
soup = BeautifulSoup(r.content, 'html.parser')
title = soup.find('a',class_='home')
a = soup.find('span',class_='artist')
s = soup.find('span',class_='song')
alb = soup.find('span',class_='release')
lab = soup.find('span',class_='parenthesis')

#Converts in strings
station = str(title.text)
artist = str(a.text)
song = str(s.text)
album = str(alb.text)
lab = str(lab.text)

print(station)
print("Song: "+ song)
print("Artist: "+ artist)
print("Album: "+ album)
print("Record Label: " + lab)

