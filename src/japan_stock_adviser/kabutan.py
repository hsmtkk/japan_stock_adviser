import sys

import bs4
import requests


def owner_benefit():
    symbol = sys.argv[1]
    url = f"https://kabutan.jp/stock/yutai?code={symbol}"
    resp = requests.get(url)
    soup = bs4.BeautifulSoup(resp.text, "html.parser")
    benefit_elem = soup.find("div", class_="stock_yutai_detail_box")
    print(benefit_elem.text)
