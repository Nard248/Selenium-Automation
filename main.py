import httpx
from selectolax.parser import HTMLParser
import pandas as pd

Listings = {
    'title' : [],
    'price': [],
    'disc' : []
}

def get_html(page):
    url = f"https://www.list.am/user/622659?c=60&pg={page}"
    resp = httpx.get(url)
    return HTMLParser(resp.text)


def parse_listings(html):
    content = html.css('div.pagecol')
    print(content)
    title = content.find_all("div.l")
    prices = content.find_all("div.p")
    disc = content.find_all("div.at")

    for t in title:
        Listings['title'].append(t.text().encode('utf-8'))

    for p in prices:
        try:
            Listings['price'].append(p.text())
        except AttributeError:
            print("atrib error")

    for d in disc:
        Listings['disc'].append(d.text())

    for i in range(len(Listings['title']) - len(Listings['price'])):
        Listings['price'].append("no price")

    for i in range(len(Listings['title']) - len(Listings['disc'])):
        Listings['disc'].append("no disc")


def main():
    for i in range(1, 3):
        html = get_html(i)
        parse_listings(html)


def dataframe(dict):
    len(dict)


if __name__ == '__main__':
    main()
    new_df = pd.DataFrame.from_dict(Listings)
    print(new_df)
#    new_df.to_csv('Asatryan Consulting apt rent.csv')

