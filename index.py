from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
from xlsxwriter import Workbook
import xlrd

# # Setting-Up User Agent
# ua = UserAgent()
# print(ua.firefox)

scrap_page = requests.get("https://codingbat.com/java")
soup = BeautifulSoup(scrap_page.content, 'lxml')

links = soup.find_all('div', attrs= {'class': "summ"}, limit= 10)

url = ['https://codingbat.com' + (link.a['href']) for link in links]

Wb = Workbook('scrap_file.xlsx')
Sh  = Wb.add_worksheet()

r = 0

for link in url:
    # For Stage 1
    quesLink = requests.get(link)
    soupQ = BeautifulSoup(quesLink.content, 'lxml')
    link1 = soupQ.find_all('td', attrs= {'width': "200"}, limit= 10)
    ques_bank_links = ["https://codingbat.com" + (i.a['href']) for i in link1]
    # for i in ques_bank_links:
    #     print(i)

    for each_Ques_link in ques_bank_links:
        each_Ques = requests.get(each_Ques_link)
        soupQ1 = BeautifulSoup(each_Ques.content, 'lxml')

        quesDes = soupQ1.find_all('p', {'class': "max2"})

        for i in quesDes:
            Sh.write(r, 0, i.string)
            print(i.string)


        outPut = soupQ1.find_all('div', {'class':"minh"})
        c = 1
        for j in outPut:
            for k in j.next_siblings:
                if k.string is not None:
                    Sh.write(r, c, k)
                    c = c+1
                    print(k)
        r = r + 1





Wb.close()