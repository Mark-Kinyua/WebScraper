from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Python_%28programming_language%29"
html_code = urlopen(url).read().decode("utf-8")

soup = BeautifulSoup(html_code, 'lxml')

type_table = soup.find(class_="wikitable")

body = type_table.find("tbody")
rows = body.find_all("tr")[1:]

mutable = []
immutable = []

for row in rows:
    data = row.find_all("td")
    if data[1].get_text() == "mutable\n":
        mutable.append(data[0].get_text())
    else:
        immutable.append(data[0].get_text())

print(f"Mutable Types: {mutable}")
print(f"Immutable Types: {immutable}")

