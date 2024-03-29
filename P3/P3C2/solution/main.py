from bs4 import BeautifulSoup

# Step 1 : Extraction of desired information with Beautiful Soup
with open("index.html", 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Extraction of the page title
title = soup.title.string

# Extraction of the text from the h1 tag
h1_text = soup.h1.string

# Extraction of the names and prices of the products in the list
products = soup.find_all('li')
products_list = []
for product in products:
    name = product.h2.string
    price = product.find('p', string=lambda s: 'Price' in s).string
    products_list.append((name, price))

# Extraction of the descriptions of the products in the list
descriptions_list = []
for product in products:
    description = product.find('p', string=lambda s: 'Description' in s).string
    descriptions_list.append(description)

# Step 2 : Displaying the extracted information
print("Title of the page :", title)
print("Text of the h1 tag :", h1_text)
print("Product list :", products_list)
print("List of product descriptions :", descriptions_list)

# Step 3 : Conversion of prices to dollars
for i, (name, price) in enumerate(products_list):
    euro_price = int(price.split()[2].replace("€",""))
    dollar_price = euro_price * 1.2
    products_list[i] = (name, f"{dollar_price}$")

# Step 4 : Displaying the new list with prices in dollars
print("List of products :", products_list)