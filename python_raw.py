import time

from fastapi import FastAPI
from selenium import webdriver
from bs4 import BeautifulSoup
import pprint
from fastapi.responses import HTMLResponse
from selenium.common.exceptions import NoSuchElementException

from setup.sheet_setup import spreadsheet

app = FastAPI()

search = f"Software Companies in Kakinada"
# finding city...
from setup.driver_Setup import browser

browser.get('https://google.com/search?q=' + search)
# opening page
browser.implicitly_wait(20)
browser.find_element_by_xpath('//*[@id="Odp5De"]/div/div/div/div[2]/div[1]/div[2]/g-more-link/a/div').click()


def get_parent():
    elem = browser.find_element_by_xpath('//*[@id="rl_ist0"]/div/div[1]/div[4]')
    _ = elem.get_attribute('innerHTML')
    _ = BeautifulSoup(_, 'html.parser')
    return _


inner_html = get_parent()

main_target = inner_html.findAll('div', {"class": "VkpGBb"})
for _ in main_target:
    time.sleep(2)

    # Name
    child_target = _.find('div', {"class": "dbg0pd OSrXXb eDIkBe"})
    company_name = child_target.find('span').getText()
    k = company_name


    # Location
    child_target = _.find('div', {"class": "rllt__details"})
    divs = child_target.findAll('div')
    for element in divs[1:]:
        company_location = element.getText()
        print(company_location)
