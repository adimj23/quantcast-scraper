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
from lxml import html


with open(r'/Users/adisrinivasan/UIUC/AutoBrowsing/FemAs.html', "r") as f:
    page = f.read()
tree = html.fromstring(page)


attributes = tree.findall(".//div[@class='c7O9k']")

for item in attributes:
    print(item.text_content())

# gc = gspread.service_account(filename="/Users/adisrinivasan/UIUC/AutoBrowsing/creds.json")
# sh = gc.open(SHEET_NAME).sheet1

