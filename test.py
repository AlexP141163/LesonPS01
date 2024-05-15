from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get("https://www.wikipedia.org/")
time.sleep(10)
browser.quit()
