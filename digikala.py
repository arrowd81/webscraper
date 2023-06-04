import requests
from bs4 import BeautifulSoup
import csv

# Send a GET request to the website
url = "https://www.digikala.com/search/mobile-phone/"
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Extract product information
products = soup.find_all("div", class_="product-list_ProductList__item__LiiNI")

# Save the product information in a CSV file
links = "links.csv"
with open(links, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["link"])  # Write header row
    for product in products:
        writer.writerow([product.get("href")])