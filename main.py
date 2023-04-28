from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/tables"
html_code = urlopen(url).read().decode("utf-8")

# print(html_code)
# start = html_code.find("<h1>") + len("<h1>")
# end = html_code.find("</h1>")
# print(html_code[start:end])

soup = BeautifulSoup(html_code, features="lxml")

# h2_headings = soup.find_all("h2")
# print(h2_headings)
#
# images = soup.find_all("img")
# print(images)
# print(images[1]['src'])

first_table = soup.find('table')
rows = first_table.find_all('tr')[1:]

last_names = []

for row in rows:
    last_names.append(row.findAll('td')[2].get_text())

print(last_names)






