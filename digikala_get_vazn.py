from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

# Specify the file path
file_path = "links.csv"

# Open the file in read mode
with open(file_path, 'r') as csvfile:
    reader = csv.reader(csvfile)

    # Read each row of the CSV file
    for row in reader:
        print(row)

