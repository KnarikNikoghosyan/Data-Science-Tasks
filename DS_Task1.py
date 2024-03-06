import requests
from bs4 import BeautifulSoup

def fetch_wikipedia_content(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            content_div = soup.find('div', {'id': 'mw-content-text'})
            paragraphs = content_div.find_all('p')
            content = '\n'.join([p.get_text() for p in paragraphs])
            print(content)
        else:
            print(f"Error: Unable to fetch content from {url}. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    url = input("Enter the URL of the Wikipedia page: ")
    fetch_wikipedia_content(url)