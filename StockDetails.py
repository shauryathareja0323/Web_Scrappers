from bs4 import BeautifulSoup as bs
from selenium import webdriver
import re

driver=webdriver.Chrome()

s_name=input("Enter the stock name: ")

driver.get(f"https://www.screener.in/company/{s_name}")
stockPage=driver.page_source
stockPageHTML=bs(stockPage,'html.parser')

stocksBigBox=stockPageHTML.find_all("li", {"class":"flex flex-space-between"})

marketCapData=stocksBigBox[0]
marketCapSpan=marketCapData.find_all("span",{"class":"nowrap value"})
marketCapSpan2=marketCapSpan[0]
marketCap=marketCapSpan2.find_all("span",{"class":"number"})

StockPEData=stocksBigBox[3]
StockPESpan=StockPEData.find_all("span",{"class":"nowrap value"})
StockPESpan2=StockPESpan[0]
StockPE=StockPESpan2.find_all("span",{"class":"number"})

BookValueData=stocksBigBox[4]
BookValueSpan=BookValueData.find_all("span",{"class":"nowrap value"})
BookValueSpan2=BookValueSpan[0]
BookValue=BookValueSpan2.find_all("span",{"class":"number"})




print("Market cap is: Rs.",marketCap[0].text,"Cr")
print("Stock PE is:",StockPE[0].text)
print("Book Value is: Rs.",BookValue[0].text)

