import requests
import json
import csv

def getVazn(url):
  arrayout = ["","<==name vanz==>",""]

  response = requests.get(url)

  data = response.json()

  #get name
  itemname = data['data']['product']['title_fa']
  arrayout[0] = itemname

  #getvazn
  itemvazn = data['data']['product']['specifications'][0]['attributes']
  arrayout[2] = itemvazn[1]['values'][0]

  return arrayout

# print(getVazn("https://api.digikala.com/v1/product/352451/"))
# Specify the file path
file_path = "links.csv"
pruduct_path = "result.csv"
headurl = "https://api.digikala.com/v1/product/"
with open(pruduct_path, 'w', newline='' , encoding='utf-8') as csvfilew:
  writer = csv.writer(csvfilew)
  # Open the file in read mode
  with open(file_path, 'r' , encoding='utf-8') as csvfiler:
    reader = csv.reader(csvfiler)
    # Read each row of the CSV file
    # rownumber = len(list(reader))
    for row in reader:
      if row[0].startswith("/"):
        product_id_end = row[0].find("/", 13) + 1
        url = (headurl + row[0][13:product_id_end])
        writer.writerow(getVazn(url))
      print(f"getting item number {reader.line_num}")


