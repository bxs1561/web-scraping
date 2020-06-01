from bs4 import BeautifulSoup
# from urllib.request import urlopen as uReq
import urllib.request
import lxml
import requests;

import pandas as pd

quote_page = 'https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
# http = urllib3.PoolManager()
# page = http.urlopen("GET", quote_page)
# soups = soup(page, 'html.parser')
#
# name_box = soup.find('h1', attrs={'class': 'price'})
# price = price_box.text
# page = requests.get(quote_page)
# soups = BeautifulSoup(requests.get(quote_page).text, 'lxml')
# name_box = soups.find('h3', attrs={'class': 'info__heading'})
# name = name_box.text.strip()
# print(soups)
# containers = page_soup.find_all("div", {"class": "col _2-gKeQ"})




# this works
response = requests.get(quote_page)
html = response.content
soup = BeautifulSoup(html, 'html.parser')

# page = urllib.request.urlopen(quote_page).read()
# soup = BeautifulSoup(page, 'lxml')
name_box = soup.findAll('div', {'class': '_3O0U0u'})
# name_box = soup.findAll('div', {'class': 'bhgxx2 col-12-12'})

name = name_box[0]
# red = page.read()

# print(BeautifulSoup.prettify(name_box[0]))
# print(name.div.img['alt'])
# price = name.findAll('div', {'class': '_3Uy12X'})
price = name.findAll('div', {'class': '_1uv9Cb'})

rating = name.findAll('div', {'class': 'niH0FQ _36Fcw_'})

# print(BeautifulSoup.prettify(rating[0]))
filename = 'products.csv'
file = open(filename, "w")
headers = "Product_Name,                        Pricing,     Ratings\n "
file.write(headers)

for nam in name:
    product_name = nam.div.img["alt"]
    price_cont = nam.findAll('div', {'class': '_1uv9Cb'})
    price = price_cont[0].text.strip()

    rating_cont = name.findAll('div', {'class': 'niH0FQ _36Fcw_'})
    rating = rating_cont[0].text


    #string parsing
    trim_price = ''.join(price)
    rupee = trim_price.split("₹")
    add_rs = "Rs." + rupee[1]
    split_price = add_rs.split("E")
    final_price = split_price[0]

    split_rating = rating.split(" ")
    final_rating = split_rating[0]

    # print("product name" + product_name)
    # print("price" + final_price)
    # print("rating" + final_rating)

    print(product_name.replace(',', '|') + ',' + " " + final_price+','+final_rating+'\n')
    file.write(product_name.replace(',', '|') + ',' + "     " + final_price+',' +  "    "+final_rating+'\n')

file.close()



# print(file)