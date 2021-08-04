import time
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.options import Options
from info import DRIVER_PATH, SHEET_NAME, USERNAME, PASSWORD
from datetime import datetime
import gspread


# websites = ["ballotpedia.org", "baseball-reference.com", "basketball-reference.com", "brainly.com", 
# "britannica.com", "bustle.com", "buzzfeed.com", "campingworld.com", "cars.com"]
websites = ["google.com"]

my_options = Options()
my_options.headless = False
my_options.add_argument("--incognito")
driver = webdriver.Chrome(DRIVER_PATH, options=my_options)

gc = gspread.service_account(filename="/Users/adisrinivasan/UIUC/AutoBrowsing/creds.json")
sh = gc.open(SHEET_NAME).sheet1

driver.get("https://adssettings.google.com/authenticated")

email_field = driver.find_element_by_xpath("//input[@type='email']")
email_field.send_keys(USERNAME)
driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button').click()
