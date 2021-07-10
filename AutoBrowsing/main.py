import time
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.options import Options
from info import DRIVER_PATH
from datetime import datetime


# websites = ["ballotpedia.org", "baseball-reference.com", "basketball-reference.com", "brainly.com", 
# "britannica.com", "bustle.com", "buzzfeed.com", "campingworld.com", "cars.com"]
websites = ["google.com"]

my_options = Options()
my_options.headless = False
my_options.add_argument("--incognito")
my_options.binary_location = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
driver = webdriver.Chrome(DRIVER_PATH, options=my_options)



driver.get("https://www.google.com")
