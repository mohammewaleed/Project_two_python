import requests
from bs4 import BeautifulSoup
respones = requests.get("https://books.toscrape.com")


soup = BeautifulSoup(respones.content, 'html.parser')

books = soup.find_all("article")

for book in books :
  title = book.h3.a["title"]
  rating = book.p["class"][1]

  print("Name of book: " + title)
  print("Rating is: " + rating)