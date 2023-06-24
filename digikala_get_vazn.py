import requests
import json
import csv
import config
import constant

def get_weight(url):
  arrayout = ["",""]

  response = requests.get(url)

  data = response.json()

  #get name
  itemname = data['data']['product']['title_fa']
  arrayout[0] = itemname

  #get weight
  item_attributes = data['data']['product']['specifications'][0]['attributes']
  itemvazn = ""
  found = False
  index = 0
  while((not found) and index <= len(item_attributes)):
    if item_attributes[index]['title'] == 'وزن':
      found = True
      itemvazn = item_attributes[index]['values'][0]
    else:
      index += 1

  arrayout[1] = itemvazn.replace('گرم', '').strip()

  return arrayout

def read_links():
  links = []
  with open(config.links_path, 'r' , encoding='utf-8') as csvfiler:
    reader = csv.reader(csvfiler)
    for row in reader:
      if row[0].startswith("/"):
        links.append(row)
  return links

def write_data(links):
  all_data = []
  for i, link in enumerate(links):
    product_id_end = link[0].find("/", 13) + 1
    url = (constant.head_url + link[0][13:product_id_end])
    all_data.append(get_weight(url))
    print(f"getting item number {i}")

  with open(config.result_path, 'w', newline='' , encoding='utf-8') as csvfilew:
    writer = csv.writer(csvfilew)
    for data in all_data:
      writer.writerow(data)

if __name__ == "__main__":
  write_data(read_links())
