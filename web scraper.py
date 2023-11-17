import requests;
from bs4 import BeautifulSoup;
website = input("Enter an url to scraping")
requset = requests.get(url = website)

if requset.status_code == 200 :
  soup = BeautifulSoup(requset.text, 'html.parser')
  heading_3 = soup.find_all('h3')
  for h3 in heading_3 :
    print("your Head:" , h3.text)
  articl = soup.find('article', class_= 'product_pod')
  para = articl.find('p' , class_= 'star-rating')
  Rating = para.find ('i', class_='icon-star')
  print("Rating: ", Rating.text)