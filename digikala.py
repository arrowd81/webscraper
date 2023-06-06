from selenium import webdriver
from bs4 import BeautifulSoup
import time


webdriver_path = "E:/Projects/webscraping/chromedriver.exe"
out=[]
gonext = True
minPrice = 1
maxPrice = 5000000

# while gonext:

url = "https://www.digikala.com/search/mobile-phone/?page=1"

# Configure the web driver
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path=webdriver_path, options=options)
# Load the webpage
driver.get(url)

time.sleep(15)
# Get the page source after JavaScript rendering
page_source = driver.page_source

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(page_source, "html.parser")
# Find all the anchor tags (<a>) in the parsed HTML

anchor_tags = soup.find_all("a" , class_ = "d-block pointer pos-relative bg-000 overflow-hidden grow-1 py-3 px-4 px-2-lg h-full-md styles_VerticalProductCard--hover__ud7aD")

# Extract the href attribute from each anchor tag
links = [a.get("href") for a in anchor_tags if a.get("href")]

if len(links) < 20:
    gonext = False
# Print all the links
for link in links:
    out.append(link)
# Close the web driver
driver.quit()

print(len(out))
