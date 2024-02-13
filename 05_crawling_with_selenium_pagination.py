# You can use ctrl F at inpection option on navigator in order
# to check the xpath of this program
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

import pandas as pd

website = "https://www.audible.com./adblbestsellers?ref_pageloadid=9QLzjXNwlj46IFF2&ref=a_adblbests_b1_desktop_footer_column_2_0&pf_rd_p=6a55a63d-48d3-4d5e-857f-ae6682380e4d&pf_rd_r=NNKNEEHS01GTZBZW1JYX&pageLoadId=z5UBqzwr0JNDjRg6&creativeId=2d835e86-1f10-4f6e-a4c6-33d2001684e6"
path = "C:/Users/lucca/PycharmProjects/chromedriver.exe"

# Configuração das opções do navegador
options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
options.add_experimental_option("detach", True)

# Inicialização do webdriver
driver = webdriver.Chrome(options=options, service=Service(path))

# Navegação para a página web
driver.get(website)

# Pagination
pagination = driver.find_element("xpath", '//ul[contains(@class,"pagingElements")]')
pages = pagination.find_elements("xpath", './/li[contains(@class,"bc-list-item")]')
print(pages[-2].text)
last_page = int(pages[-2].text)

book_title = []
book_author = []
book_length = []

current_page = 1
while current_page <= last_page:
    time.sleep(2)
    container = driver.find_element("xpath", '//div[contains(@class,"adbl-impression-container")]')
    products = container.find_elements("xpath", './/li[contains(@class,"productListItem")]')

    for product in products:
        book_title.append(product.find_element("xpath", './/h3[contains(@class,"bc-heading")]').text)
        book_author.append(product.find_element("xpath", './/li[contains(@class,"authorLabel")]').text)
        book_length.append(product.find_element("xpath", './/li[contains(@class,"runtimeLabel")]').text)

    current_page += 1

    try:
        next_page = driver.find_element("xpath", '//span[contains(@class,"nextButton")]')
        next_page.click()
    except:
        pass

# Fechamento do navegador após a conclusão das tarefas
driver.quit()

df = pd.DataFrame({"title": book_title, "author": book_author, "lenght": book_length})
df.to_csv("audible_books_headless.csv", index=False)

print("Web scrapping is done.")

