# This is a Python Web scraper using the selenium library and the thing to be scraping is a value 
# from an html element which will be the current price of Etherium on the coinmarketcap website
## All Selenium Imports Inline with the new Selenium 4 release
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# With selenium4 as the key executable_path is deprecated we have to use an instance of the Service() class 
# along with ChromeDriverManager().install() command
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# This gets the webpage of which I want to preform the webscrapping on. It will open chrome and go to the webpage
driver.get("https://coinmarketcap.com/currencies/ethereum/")

# After looking through coinmarketcap's html code of their webpage via developer tools, I found the html element
# for the etherium price and it was represented by a specific class name of "priceValue" which I was able to use 
# to locate and get the element to report etherium's current price.
search = driver.find_element(By.CLASS_NAME, "priceValue")
# This prints the webpage's title in the terminal so you can see this relates to etherium's current price
# represented in USD from coin market cap
print(driver.title)
# This print's the text (or value (which contains the price of Etherium)) inside of "search" 
# giving us the the html element represented by the class name "priceValue"
print(search.text)

# This closes the driver and also closes the chrome page
driver.quit()