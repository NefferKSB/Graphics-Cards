import xlsxwriter
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#######~GeForce RTX 30 Series~########
print('triggered')
page_num = 0
my_url = "https://www.bestbuy.com/site/searchpage.jsp?_dyncharset=UTF-8&cp=" + str(page_num) + "id=pcat17071&iht=y&keys=keys&ks=960&list=n&qp=gpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~NVIDIA%20GeForce%20RTX%203060%5Egpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~NVIDIA%20GeForce%20RTX%203060%20Ti%5Egpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~NVIDIA%20GeForce%20RTX%203070%5Egpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~NVIDIA%20GeForce%20RTX%203080%5Egpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~NVIDIA%20GeForce%20RTX%203090&sc=Global&st=graphics%20card&type=page&usc=All%20Categories" 
print(my_url)

#Opening up connection, grabbing the page
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
uClient = uReq('https://www.bestbuy.com/site/searchpage.jsp?_dyncharset=UTF-8&id=pcat17071&iht=y&keys=keys&ks=960&list=n&qp=category_facet%3Dname~abcat0507002%5Egpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~NVIDIA%20GeForce%20RTX%203060%5Egpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~NVIDIA%20GeForce%20RTX%203060%20Ti%5Egpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~NVIDIA%20GeForce%20RTX%203070%5Egpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~NVIDIA%20GeForce%20RTX%203080%5Egpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~NVIDIA%20GeForce%20RTX%203090&sc=Global&st=graphics%20card&type=page&usc=All%20Categories')
page_html = uClient.read()
page_soup = soup(page_html, "html.parser")
uClient.close()


#HTML parsing
#page_soup = soup(page_html, "html.parser")
print('triggered 2')
#print('triggered 2a ' + page_soup)

#page_number = page_soup.findAll("li", {"class": "page-item"})
print('triggered 3')
#uClient.close()
# last_div = None
# for last_div in page_number:pass
# if last_div:
#     content = last_div.getText()
#     print(content)
#Grabs the current and total pages
# page_element = page_soup.findAll("span", {"class": "list-tool-pagination-text"})
# page_element_text = page_element[0].text
# page_number_text = page_element_text.split(' ')[1]
# page_number_text_count = page_number_text.split('/')

#total_pages = int(page_number_text_count[1])

# Create a workbook and add a worksheet.
# now = datetime.now()
# dt_string = now.strftime("%d-%m-%Y %Hhr %Mmin")
# newEggWorkbook = xlsxwriter.Workbook("newEggGraphicsCard_"+dt_string+".xlsx")
# newEggWorksheet = newEggWorkbook.add_worksheet()

# Start from the first cell. Rows and columns are zero indexed.
# row = 0
# col = 0

# while page_num < 3:
    
#     page_num += 1
#     my_url = 'https://www.newegg.com/p/pl?N=100007709%20601357282&page=' + str(page_num)
#     print(my_url)

#     #Opening up connection, grabbing the page
#     uClient = uReq(my_url)
#     page_html = uClient.read()

#     #HTML parsing
#     page_soup = soup(page_html, "html.parser")

#     #Grabs each product
#     containers = page_soup.findAll("div", {"class": "item-container"})

#     for container in containers: 
#         #Stock
#         stock = container.findAll("p", {"class":"item-promo"})[0].text
#         #Check to see if there is available stock first, if yes print the Graphics card info

#         if stock != "OUT OF STOCK":
#             #Graphics card make
#             if hasattr(container.div.div, "a") and hasattr(container.div.div.a.img, "title"):
#                 make = container.div.div.a.img["title"]
#             else:
#                 make = "Make is unknown"

#             #Graphics card name
#             name_container = container.findAll("a", {"class":"item-title"})
#             graphics_card_name = name_container[0].text
            
#             #Shipping cost
#             shipping_container = container.findAll("li", {"class":"price-ship"})
#             shipping = shipping_container[0].text.strip()

#             #Link to Graphics card
#             item_title = container.div.findAll("a", {"class":"item-title"})
#             link = item_title[0]["href"]

#             print("")
#             print("")
#             print("")
#             print("")

#             #newEggWorksheet.write(row, col, make)
#             #newEggWorksheet.write(row, col + 1, graphics_card_name)
#             #newEggWorksheet.write(row, col + 2, stock)
#             #newEggWorksheet.write(row, col + 3, shipping)
#             #newEggWorksheet.write(row, col + 4, link)
#             #row += 1
# uClient.close()
#######~GeForce RTX 30 Series End~########

#newEggWorkbook.close()