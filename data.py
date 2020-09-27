import requests
from bs4 import BeautifulSoup as Bs

response = requests.get('https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%D0%B8%D0%B5%D0%B2/2020-07-18')
soup = Bs(response.content, 'html.parser')
item = soup.find('div', class_ = 'min',).get_text(strip = True)