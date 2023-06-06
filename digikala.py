from selenium import webdriver
from bs4 import BeautifulSoup
import time


webdriver_path = "E:/Projects/webscraping/chromedriver.exe"
out=[]
nextpage = True
nextprice = True
minPrice = 1
maxPrice = 500000
while nextprice:
    pagenum = 1
    while nextpage:
        url = f"https://www.digikala.com/search/category-mobile-phone/product-list/?page={pagenum}&price%5Bmax%5D={maxPrice}0&price%5Bmin%5D={minPrice}0"

        # Configure the web driver
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(executable_path=webdriver_path, options=options)
        # Load the webpage
        driver.get(url)

        time.sleep(5)

        # Get the page source after JavaScript rendering
        page_source = driver.page_source

        # Create a BeautifulSoup object to parse the HTML content
        soup = BeautifulSoup(page_source, "html.parser")
        # Find all the anchor tags (<a>) in the parsed HTML

        anchor_tags = soup.find_all("a" , class_ = "d-block pointer pos-relative bg-000 overflow-hidden grow-1 py-3 px-4 px-2-lg h-full-md styles_VerticalProductCard--hover__ud7aD")

        # Extract the href attribute from each anchor tag
        links = [a.get("href") for a in anchor_tags if a.get("href")]

        if len(links) < 20:
            nextpage = False
        else:
            pagenum += 1
        
        # Print all the links
        for link in links:
            out.append(link)
        # Close the web driver
        driver.quit()

    if maxPrice < 10000000 :
        minPrice += 500000
        maxPrice += 500000
        nextpage = True
    else:
        nextprice = False

print(len(out))
