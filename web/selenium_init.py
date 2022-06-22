
import time
import pandas as pd
import numpy as np

from lxml import html
from lxml.cssselect import CSSSelector

# Create the web driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


from selenium.webdriver.chrome.service import Service
from selenium import webdriver

service = Service(executable_path="/SeleniumDrviers/chromedriver.exe")
driver = webdriver.Chrome(service=service)


def get_top_axies(top):
    
    gathered = 0
    pos = 0 
    url = f'https://tracker.axie.management/leaderboard/origin?position={pos}'
    print(url)
    while gathered < top:

        driver.get(url)
        driver.implicitly_wait(30)

        links = WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a[href*="origin"]')))

        results = []

        for link in links:
            tostr = str(link.get_attribute('href'))
            if 'battles' in tostr and 'origin' in tostr:
                results.append(tostr)
        
        pos += len(results)
        print(pos)
        time.sleep(5)
        
        driver.quit()
        driver.close()
        
get_top_axies(100)