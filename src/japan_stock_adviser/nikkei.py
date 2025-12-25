import urllib.request
import sys

import bs4
import fake_useragent


def list_symbols():
    symbol = sys.argv[1]
    url = f"https://indexes.nikkei.co.jp/nkave/index/component?idx={symbol}"
    req = urllib.request.Request(url)
    req.add_header("User-Agent", fake_useragent.UserAgent().chrome)
    with urllib.request.urlopen(req) as f:
        content = f.read()

    soup = bs4.BeautifulSoup(content.decode(), "html.parser")
    idx_section = soup.find("section", class_="idx-section")
    print(idx_section)
