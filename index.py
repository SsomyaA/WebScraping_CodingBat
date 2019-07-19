from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

# # Setting-Up User Agent
# ua = UserAgent()
# print(ua.chrome)

scrap_page = requests.get("https://codingbat.com/java")
soup = BeautifulSoup(scrap_page.content, 'lxml')

links = soup.find_all('div', attrs= {'class': "summ"})


url = ['https://codingbat.com' + (link.a['href']) for link in links]

print(url)
