import xlsxwriter
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

# Create a workbook and add a worksheet.
newEggWorkbook = xlsxwriter.Workbook('newEggGraphicsCard.xlsx')
newEggWorksheet = newEggWorkbook.add_worksheet()

# Start from the first cell. Rows and columns are zero indexed.
row = 0
col = 0

headers = "make, graphics_card_name, stock, shipping_price, link\n"

for container in containers: 
    #Stock
    stock = container.findAll("p", {"class":"item-promo"})[0].text
    #Check to see if there is available stock first, if yes print the Graphics card info

    #Graphics card make
    if hasattr(container.div.div, "a"):
        make = container.div.div.a.img["title"]
    else:
        make = "Make is unknown"

    #Graphics card name
    name_container = container.findAll("a", {"class":"item-title"})
    graphics_card_name = name_container[0].text

    #Shipping cost
    shipping_container = container.findAll("li", {"class":"price-ship"})
    shipping = shipping_container[0].text.strip()

    #Link to Graphics card
    item_info = container.findAll("div", {"class":"item-info"})
    link = item_info[0].a["href"]

    print("make: " + make)
    print("graphics card name: " + graphics_card_name)
    print("stock: " + stock)
    print("shipping: " + shipping)
    print("link: " + link)

    newEggWorksheet.write(row, col, make)
    newEggWorksheet.write(row, col + 1, graphics_card_name)
    newEggWorksheet.write(row, col + 2, stock)
    newEggWorksheet.write(row, col + 3, shipping)
    newEggWorksheet.write(row, col + 4, link)
    row += 1
    
newEggWorkbook.close()