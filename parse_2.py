import requests
from pprint import pprint
from bs4 import BeautifulSoup

url = "https://ru.wikipedia.org/wiki/%D0%9C%D0%B0%D0%B3%D0%B0%D0%B4%D0%B0%D0%BD"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
q = soup.find_all("div", class_="mw-parser-output")

file = open("file", "w", encodings="UTF-8")
file.write(q[0].text)
file.close()

# with open('file', 'w') as output_file:
#     output_file.write(response.text)
