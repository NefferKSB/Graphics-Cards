import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/p/pl?d=nvidia+3080+graphics+card&N=100007709&cm_sp=Category-_-INFOCARD-_-nvidia+3080+graphics+card-_-L48-_-1&name=Desktop-Graphics-Cards'

#Opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#HTML parsing
page_soup = soup(page_html, "html.parser")

#Graps each product
containers = page_soup.findAll("div", {"class": "item-container"})

filename = "graphicsCards.csv"
f = open(filename, "w")
headers = "make, graphics_card_name, shipping_price\n"

f.write("")

for container in containers:
    make = container.div.div.a.img["title"]

    name_container = container.findAll("a", {"class":"item-title"})
    graphics_card_name = name_container[0].text

    shipping_container = container.findAll("li", {"class":"price-ship"})
    shipping = shipping_container[0].text.strip()

    print("make: " + make)
    print("graphics card name: " + graphics_card_name)
    print("shipping: " + shipping)

    f.write(make + "," + graphics_card_name.replace(",", "|") + "," + shipping + "\n")
f.close()