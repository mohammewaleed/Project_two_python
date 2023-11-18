import requests;
from bs4 import BeautifulSoup;
respones = requests.get("https://books.toscrape.com/")

if respones.status_code == 200 :
  soup = BeautifulSoup(respones.content, 'html.parser')

  articles = soup.find_all('article', class_= 'product_pod')

  for article in articles:
    title = article.h3.a['title']
    print("Title of book: " + title)
    rating = article.p["class"][1]
    print ("Ratig: " + rating )