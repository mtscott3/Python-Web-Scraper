# Web scrape with Python and the thing to be scraping is a value from an html element 
# in coinmarketcap website
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://coinmarketcap.com/currencies/ethereum/")

search = driver.find_element(By.CLASS_NAME, "priceValue")
print(driver.title)
print(search.text)

driver.quit()