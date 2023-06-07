from bs4 import BeautifulSoup
import requests
import json
import csv

nextpage = True
nextprice = True
minPrice = 1
maxPrice = 500000

linkfile = open("links.csv" , "w" , encoding='utf-8')
writer = csv.writer(linkfile , lineterminator='\n' ,)

while nextprice:
    pagenum = 1
    while nextpage:
        url = f"https://api.digikala.com/v1/categories/mobile-phone/search/?price%5Bmax%5D={maxPrice}0&price%5Bmin%5D={minPrice}0&seo_url=%2Fcategory-mobile-phone%2Fproduct-list%2F%3Fprice%255bmax%255d%3D20000000%26price%255bmin%255d%3D0&page={pagenum}"

        response = requests.get(url)

        data = response.json()
        
        products = data['data']['products']

        if len(products) < 20:
            nextpage = False
        else:
            pagenum += 1
        
        for product in products:
            link = product["url"]["uri"]
            writer.writerow([link])

    if maxPrice <= 100000000 :
        minPrice += 500000
        maxPrice += 500000
        nextpage = True
    else:
        nextprice = False
    print(f"progress = {maxPrice/1000000} %")


linkfile.close()