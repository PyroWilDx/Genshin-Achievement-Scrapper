import requests
from bs4 import BeautifulSoup


def getAllTextWeb(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        all_text = soup.get_text(separator="\n", strip=True)

        return all_text
    else:
        print(f"Error: Unable to fetch content from {url}. Status code : {response.status_code}")
        return None
