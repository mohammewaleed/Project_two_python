import requests
from bs4 import BeautifulSoup

def get_soup(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses.
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup
    except requests.RequestException as e:
        print(f"Error making the request: {e}")
        return None

def extract_books_info(soup):
    if soup is None:
        return

    articles = soup.find_all('article', class_='product_pod')

    for article in articles:
        try:
            title = article.h3.a['title']
            rating = article.p["class"][1]
            print(f"Title of book: {title}\nRating: {rating}\n")
        except (AttributeError, KeyError) as e:
            print(f"Error extracting book information: {e}")

def main():
    url = "https://books.toscrape.com/"
    soup = get_soup(url)
    extract_books_info(soup)

if __name__ == "__main__":
    main()
