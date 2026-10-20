import requests
from datetime import datetime
from bs4 import BeautifulSoup

# #Debug code because I'm lazy
# urlIN = "https://spinitron.com/WRAS/"
# loc = "/home/caleb-b/PycharmProjects/Spinitron-Scraper/output.txt"

urlIN = input("Type in a URL: ")
r= requests.get(urlIN)

#prints status code
print("Status Code: ",r)

#Gets time
time = str(datetime.now().strftime('%I:%M%P'))

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

#Printing info
print(station, end=' ')
print(time)
print("Song: "+ song)
print("Artist: "+ artist)
print("Album: "+ album)
print("Record Label: " + lab)

#Saving info to a file
choice = input("\nDo you want to save to a file(y/n): ")
match choice:
    case "y":
        loc = input("Where do you want to save: ")
        f1 = open(loc,"a")
        f1.writelines(time)
        f1.write(" ")
        f1.write("Song:")
        f1.write(song)
        f1.write(" Album:")
        f1.write(album)
        f1.write(" Artist:")
        f1.write(artist)
        f1.write("\n")
    case "n":
        print("Exiting")
    case _:
        print("Invalid input")