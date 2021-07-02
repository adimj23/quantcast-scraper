from login_creds import ID, PW
from selenium import webdriver

def login(driver):
    # get IC login
    driver.get("https://www.quantcast.com/user/login")
    username = driver.find_element_by_id("okta-signin-username")
    password = driver.find_element_by_id("okta-signin-password")
    username.send_keys(ID)
    password.send_keys(PW)
    driver.find_element_by_xpath("//input[@type='submit']").click()