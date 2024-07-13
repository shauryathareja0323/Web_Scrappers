#This can scrap Top News Headlines of India for you.

from bs4 import BeautifulSoup as bs
from selenium import webdriver

driver=webdriver.Chrome()

driver.get("https://www.hindustantimes.com/india-news")
newsPage=driver.page_source
newsPageHTML=bs(newsPage,'html.parser')

newsBigBox=newsPageHTML.findAll("div", {"class":"cartHolder listView track timeAgo articleClick"})

for box in newsBigBox:
    heading=box.find_all('h3',{'class':'hdg3'})[0].text
    desc=box.find_all('h2',{'class':'sortDec'})[0].text
    print(heading)
    print(desc)
    print("\n\n\n")


