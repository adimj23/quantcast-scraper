import time
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.options import Options
from info import SHEET_NAME, DRIVER_PATH
from datetime import datetime
import gspread

websites = ["ballotpedia.org", "baseball-reference.com", "basketball-reference.com", "brainly.com", 
"britannica.com", "bustle.com", "buzzfeed.com", "campingworld.com", "cars.com"]



my_options = webdriver.ChromeOptions()
my_options.headless = False
driver = webdriver.Chrome(DRIVER_PATH, options=my_options)

gc = gspread.service_account(filename="creds.json")
sh = gc.open(SHEET_NAME).sheet1


driver.get("https://www.quantcast.com/user/login")
# Wait for page to load after logging in
WebDriverWait(driver, 100).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="qcDashboard"]/header/h2'))
)

# driver.get("https://www.quantcast.com/measure/properties/")
# time.sleep(1)
for website in websites:
    demos_row = []
    demos_row.append(website)
    time.sleep(5)
    url_name = driver.find_element_by_xpath("//input[@type='search' and @placeholder='Enter a URL']")
    url_name.send_keys(website)

    driver.find_element_by_xpath("//input[@type='submit' and @value='Search']").click()

    time.sleep(20)
    
    # WebDriverWait(driver, 25).until(
    #     EC.presence_of_element_located((By.CLASS_NAME, 'table__header table__header--align-left'))
    # )

    # driver.find_element_by_link_text(websites[0]).click()

    try:
        time.sleep(5)
        driver.find_element_by_link_text(website).click()
        time.sleep(10)
        try:

            # Appending gender shares + indices, respectively
            for i in range(2,4):
                demos_row.append(float(driver.find_element_by_xpath('//*[@id="tab-title_undefined_DEMOGRAPHICS"]/div/div[2]/article/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[3]/div[' + str(i) + ']/div/h4').text.strip("%"))/100)

            for i in range(2,4):
                demos_row.append(driver.find_element_by_xpath('//*[@id="tab-title_undefined_DEMOGRAPHICS"]/div/div[2]/article/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[2]/div[' + str(i) + ']/div/h4').text)
            
            # Appending all age-range shares + indices
            for i in range(2,13):
                demos_row.append(float(driver.find_element_by_xpath('//*[@id="tab-title_undefined_DEMOGRAPHICS"]/div/div[2]/article/div[2]/div/div/div/div[1]/div[2]/div/div/div/div[3]/div[' + str(i) + ']/div/h4').text.strip("%"))/100)
            
            for i in range(2,13):
                demos_row.append(driver.find_element_by_xpath('//*[@id="tab-title_undefined_DEMOGRAPHICS"]/div/div[2]/article/div[2]/div/div/div/div[1]/div[2]/div/div/div/div[2]/div[' + str(i) + ']/div/h4').text)
            
            # Appending income shares + indices
            for i in range(2,6):
                demos_row.append(float(driver.find_element_by_xpath('//*[@id="tab-title_undefined_DEMOGRAPHICS"]/div/div[2]/article/div[2]/div/div/div/div[2]/div[1]/div/div/div/div[3]/div[' + str(i) + ']/div/h4').text.strip("%"))/100)

            for i in range(2,6):
                demos_row.append(driver.find_element_by_xpath('//*[@id="tab-title_undefined_DEMOGRAPHICS"]/div/div[2]/article/div[2]/div/div/div/div[2]/div[1]/div/div/div/div[2]/div[' + str(i) + ']/div/h4').text)

            # Appending children shares + indices
            for i in range(2,4):
                demos_row.append(float(driver.find_element_by_xpath('//*[@id="tab-title_undefined_DEMOGRAPHICS"]/div/div[2]/article/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[' + str(i) + ']/div/h4').text.strip("%"))/100)

            for i in range(2,4):
                demos_row.append(driver.find_element_by_xpath('//*[@id="tab-title_undefined_DEMOGRAPHICS"]/div/div[2]/article/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[' + str(i) + ']/div/h4').text)

            # Appending ethnicity shares + indices
            for i in range(2,7):
                demos_row.append(float(driver.find_element_by_xpath('//*[@id="tab-title_undefined_DEMOGRAPHICS"]/div/div[2]/article/div[2]/div/div/div/div[2]/div[3]/div/div/div/div[3]/div[' + str(i) + ']/div/h4').text.strip("%"))/100)

            for i in range(2,7):
                demos_row.append(driver.find_element_by_xpath('//*[@id="tab-title_undefined_DEMOGRAPHICS"]/div/div[2]/article/div[2]/div/div/div/div[2]/div[3]/div/div/div/div[2]/div[' + str(i) + ']/div/h4').text)

            # Appending education shares + indices
            for i in range(2,5):
                demos_row.append(float(driver.find_element_by_xpath('//*[@id="tab-title_undefined_DEMOGRAPHICS"]/div/div[2]/article/div[2]/div/div/div/div[1]/div[3]/div/div/div/div[3]/div[' + str(i) + ']/div/h4').text.strip("%"))/100)

            for i in range(2,5):
                demos_row.append(driver.find_element_by_xpath('//*[@id="tab-title_undefined_DEMOGRAPHICS"]/div/div[2]/article/div[2]/div/div/div/div[1]/div[3]/div/div/div/div[2]/div[' + str(i) + ']/div/h4').text)
    
            
        except NoSuchElementException:
            # Website found, but "Not Enough Data"
            driver.get("https://www.quantcast.com/measure/properties")
            continue

    except NoSuchElementException:
        # Website not found
        driver.get("https://www.quantcast.com/measure/properties/")
        continue

    
    sh.append_row(demos_row, 'USER_ENTERED')
    driver.get("https://www.quantcast.com/measure/properties/")
    time.sleep(10)