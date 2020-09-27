import requests
from bs4 import BeautifulSoup as Bs

response = requests.get('https://www.google.com/search?q=%D1%87%D0%B0%D1%81+%D1%83+%D0%BA%D0%B8%D1%94%D0%B2%D1%96&oq=%D1%87%D0%B0%D1%81+%D1%83+&aqs=chrome.0.0j69i57j0l3j69i61l3.4207j0j7&sourceid=chrome&ie=UTF-8')
soup = Bs(response.content, 'html.parser')
item3 = soup.find('div', class_ = 'gsrt vk_bk dDoNo XcVN5d',).get_text(strip = True)
print(item3)