from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

def getVazn(url):
  arrayout = ["",""]

  webdriver_path = "E:/Projects/webscraping/chromedriver.exe"

  options = webdriver.ChromeOptions()

  driver = webdriver.Chrome(executable_path=webdriver_path, options=options)

  driver.get(url)

  time.sleep(10)

  page_source = driver.page_source

  soup = BeautifulSoup(page_source, "html.parser")

  #get name
  itemname = soup.find("h1" , class_ = "text-h4 color-900 mb-2 disable-events").text
  arrayout[0] = itemname


  #getvazn
  infodiv = soup.find("div" , class_ = "w-full w-auto-lg grow-1")
  infoitem = infodiv.find_all("div" , class_ = "w-full d-flex last styles_SpecificationAttribute__valuesBox__gvZeQ")

  title = infodiv.find_all("p" , class_ = "ml-4 text-body-1 color-500 py-2 py-3-lg p-2-lg shrink-0 styles_SpecificationAttribute__value__CQ4Rz")

  for i , item in enumerate(title):
    if item.text == "وزن":
      arrayout[1] = (infoitem[i].find("p" , class_ = "d-flex ai-center w-full text-body-1 color-900 break-words").text)

  driver.quit()
  return arrayout

# print(getVazn("https://www.digikala.com/product/dkp-11410115/گوشی-موبایل-جی-ال-ایکس-مدل-2690-goldmini-plus-دو-سیم-کارت/"))

# Specify the file path
file_path = "links.csv"
pruduct_path = "result.csv"
headurl = "https://www.digikala.com"
with open(pruduct_path, 'w', newline='' , encoding='utf-8') as csvfile:
  writer = csv.writer(csvfile)
  # Open the file in read mode
  with open(file_path, 'r') as csvfile:
    reader = csv.reader(csvfile)
    # Read each row of the CSV file
    for row in reader:
      if row[0].startswith("/"):
        url = (headurl + row[0])
        writer.writerow(getVazn(url))