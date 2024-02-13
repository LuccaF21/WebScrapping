# in this project we are going to get a list of link href inside the website and scrap data from it of them.

from bs4 import BeautifulSoup
import requests
import re

root = "https://subslikescript.com"
website = f"{root}/movies"
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, "lxml")
# print(soup.prettify())

# pagination - walk through all pages with movies list
pagination = soup.find("ul", class_="pagination")
pages = pagination.find_all("li", class_="page-item")
last_page = pages[-2].text # because we have a button with ">" character that we don't need.


for page in range(1, 4): # Will run only 2 loops for testing purpose / to run all loop change int(last_page)+1
    print(page)
    result = requests.get(f"{website}?page={page}")
    content = result.text
    soup = BeautifulSoup(content, "lxml")

    box = soup.find("article", class_="main-article") #Gets one element

    links = []
    for link in box.find_all("a", href=True): #Gets all elements and return a list
        links.append(link["href"])

    for link in links:
        try:
            print(link)
            result = requests.get(f"{root}/{link}")
            content = result.text
            soup = BeautifulSoup(content, "lxml")

            box = soup.find("article", class_="main-article")

            title = box.find("h1").get_text()
            title = re.sub(r"[^\w\s]", "", title)
            transcript = box.find("div", class_="full-script").get_text(strip=True, separator=" ")

            with open(f"{title}.txt", "w", encoding="utf-8") as file:
                file.write(transcript)

        except:
            print("------link not working------")
            print(link)
            pass