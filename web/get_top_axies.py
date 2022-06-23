import time
from unittest import result
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

import csv


service = Service(executable_path="/SeleniumDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=service)


def player_loop(url=0):

    results = []
    currentUrl = f'https://tracker.axie.management/leaderboard/origin?position={url}'
    driver.get(currentUrl)
    driver.implicitly_wait(5)
    links = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a[href*="origin"]')))
    for link in links:
        tostr = str(link.get_attribute('href'))
        if 'battles' in tostr and 'origin' in tostr:
            results.append(tostr)

    time.sleep(1)
    return results
    
def get_top_players(limit):

    currentPosition = 0
    playerList = []

    while currentPosition < limit:

        results = player_loop(currentPosition)
        playerList = playerList + results
        currentPosition = currentPosition + len(results)

    return playerList

def get_top_axies(profile):

    driver.get(profile)
    driver.implicitly_wait(5)
    try:
        links = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a[href*="https://marketplace.axieinfinity.com/axie/"]')))
        axids = []
        for link in links[:3]:
            to_str = str(link.get_attribute('href'))
            splt = to_str.split('/')
            for x in splt:
                if x.isdigit():
                    axids.append(x)
        time.sleep(0.5)
        return axids
    except:
        return

def store_datas(limit):
    profileList = get_top_players(limit)

    axieList = []
    for profile in profileList:
        results = get_top_axies(profile)
        try:
            axieList = axieList + results
            print(results)
            print(axieList)
        except:
            continue

    with open('data/top_axies.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(axieList)   
    
    driver.close()

if __name__ == "__main__":
    store_datas(1000)
    
  