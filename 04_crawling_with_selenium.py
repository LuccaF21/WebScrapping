from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

country_list = []

website = "https://www.adamchoi.co.uk/overs/detailed"
path = "C:/Users/lucca/PycharmProjects/chromedriver.exe"

options = webdriver.ChromeOptions()

"""add_experimental_option("detach", True) no Selenium é usado para evitar que o navegador 
seja fechado quando o script do Selenium termina. Isso é útil quando você deseja que o navegador 
permaneça aberto após a conclusão das tarefas automatizadas."""

options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(path))
driver.maximize_window()

driver.get(website)
time.sleep(2)

# Encontra e clica em um botão
all_matches_button = driver.find_element("xpath", '//label[@analytics-event="All matches"]')
all_matches_button.click()

# Encontra e armazena informação das opções de um botão dropdown
dropdown_option = driver.find_elements("xpath", '//select[@ID="country"]/option')

for drop in dropdown_option:
    country_list.append(drop.text)

# Seleciona o dropdown de país
dropdown = Select(driver.find_element(By.ID, "country"))

for country in country_list:
    dropdown.select_by_visible_text(country)
    time.sleep(3)

    matches = driver.find_elements(By.TAG_NAME, "tr")

    date = []
    home_team = []
    score = []
    away_team = []

    for ma in matches:
        date.append(ma.find_element("xpath", './td[1]').text)
        home_team.append(ma.find_element("xpath", './td[2]').text)
        score.append(ma.find_element("xpath", './td[3]').text)
        away_team.append(ma.find_element("xpath", './td[4]').text)

    df = pd.DataFrame({"date": date, "home_team": home_team, "score": score, "away_team": away_team})
    df.to_csv(f"football_data_{country}.csv", index=False)
    print(f"{country} dataframe was exported")


print("Web scrapping is done.")
driver.quit()
