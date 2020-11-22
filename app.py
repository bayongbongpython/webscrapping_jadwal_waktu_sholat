import bs4
import requests

url = 'https://jadwalsholat.pkpu.or.id/?id=76'
contents = requests.get(url)

response = bs4.BeautifulSoup(contents.text, "html.parser")
data = response.find_all('tr', 'table_highlight')
print(data[0])

