import requests
import json
import csv
import constant
import config

def get_links(min_price, max_price):
    links = []
    while True:
        page_num = 1
        while True:
            url = f"https://api.digikala.com/v1/categories/mobile-phone/search/?price%5Bmax%5D={max_price}0&price%5Bmin%5D={min_price}0&seo_url=%2Fcategory-mobile-phone%2Fproduct-list%2F%3Fprice%255bmax%255d%3D20000000%26price%255bmin%255d%3D0&page={page_num}"
            response = requests.get(url)

            data = response.json()
            
            products = data['data']['products']

            if not products:
                break
            page_num += 1
            
            for product in products:
                link = product["url"]["uri"]
                links.append(link)

        if max_price <= config.max_price :
            min_price += config.price_interval
            max_price += config.price_interval
        else:
            break
        
        print(f"progress = {max_price/(config.max_price/100)} %" ,end='\r')

    return links

def writelinks(links):
    with open(config.links_path, 'w', encoding='utf-8') as csvfilew:
        writer = csv.writer(csvfilew , lineterminator='\n')
        for link in links:
            writer.writerow([link])

if __name__ == '__main__':
    writelinks(get_links(config.min_price, (config.min_price + config.price_interval)))