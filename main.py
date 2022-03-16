from bs4 import BeautifulSoup
import requests
import lxml


def get_page():
    request = requests.get('https://news.ycombinator.com/')
    return request.text


if __name__ == '__main__':
    html = get_page()
    soup = BeautifulSoup(html, 'lxml')

    refs = soup.find_all('a', href=True)
    news = {}
    for ref in refs:
        if ref.attrs.get('class'):
            if 'titlelink' in ref.attrs.get('class'):
                print(ref.text, '\n', ref.attrs.get('href'))
    print()
