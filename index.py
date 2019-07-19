from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

# # Setting-Up User Agent
# ua = UserAgent()
# print(ua.firefox)

scrap_page = requests.get("https://codingbat.com/java")
soup = BeautifulSoup(scrap_page.content, 'lxml')

links = soup.find_all('div', attrs= {'class': "summ"})


url = ['https://codingbat.com' + (link.a['href']) for link in links]

for link in url:
    # For Stage 1
    quesLink = requests.get(link)
    soupQ = BeautifulSoup(quesLink.content, 'lxml')
    link1 = soupQ.find_all('td', attrs= {'width': "200"})
    ques_bank_links = ["https://codingbat.com" + (i.a['href']) for i in link1]
    for i in ques_bank_links:
        print(i)
        


