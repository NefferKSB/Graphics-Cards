import xlsxwriter
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

      
page_num = 0
my_url = 'https://www.newegg.com/p/pl?N=100007709%20601357282&page=' + str(page_num)

#Opening up connection, grabbing the page
uClientInit = uReq(my_url)
page_html = uClientInit.read()

#HTML parsing
page_soup = soup(page_html, "html.parser")

#Grabs the current and total pages
page_element = page_soup.findAll("span", {"class": "list-tool-pagination-text"})
page_element_text = page_element[0].text
page_number_text = page_element_text.split(' ')[1]
page_number_text_count = page_number_text.split('/')

total_pages = int(page_number_text_count[1])

# Create a workbook and add a worksheet.
newEggWorkbook = xlsxwriter.Workbook('newEggGraphicsCard.xlsx')
newEggWorksheet = newEggWorkbook.add_worksheet()

# Start from the first cell. Rows and columns are zero indexed.
row = 0
col = 0

headers = "make, graphics_card_name, stock, shipping_price, link\n"

while page_num < total_pages:
    
    page_num += 1
    my_url = 'https://www.newegg.com/p/pl?N=100007709%20601357282&page=' + str(page_num)
    print(my_url)

    #Opening up connection, grabbing the page
    uClient = uReq(my_url)
    page_html = uClient.read()

    #HTML parsing
    page_soup = soup(page_html, "html.parser")

    #Grabs each product
    containers = page_soup.findAll("div", {"class": "item-container"})

    for container in containers: 
        #Stock
        stock = container.findAll("p", {"class":"item-promo"})[0].text
        #Check to see if there is available stock first, if yes print the Graphics card info

        if stock != "OUT OF STOCK":
            #Graphics card make
            if hasattr(container.div.div, "a") and hasattr(container.div.div.a.img, "title"):
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
            item_title = container.div.findAll("a", {"class":"item-title"})
            link = item_title[0]["href"]

            newEggWorksheet.write(row, col, make)
            newEggWorksheet.write(row, col + 1, graphics_card_name)
            newEggWorksheet.write(row, col + 2, stock)
            newEggWorksheet.write(row, col + 3, shipping)
            newEggWorksheet.write(row, col + 4, link)
            row += 1
uClient.close()
newEggWorkbook.close()