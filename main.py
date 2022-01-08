import time

from fastapi import FastAPI
from selenium import webdriver
from bs4 import BeautifulSoup
import pprint
from fastapi.responses import HTMLResponse
from selenium.common.exceptions import NoSuchElementException

from setup.sheet_setup import spreadsheet

app = FastAPI()


@app.get("/search/{city}")
async def root(city: str):
    global inner_html

    if city == 'Rajahmundry' or city == 'rajahmundry':
        sheet = spreadsheet.get_worksheet(0)
    elif city == 'Kakinada' or city == 'kakinada':
        sheet = spreadsheet.get_worksheet(1)
    else:
        sheet = spreadsheet.add_worksheet(title=f"{city}")

    search = f"Software Companies in {city}"
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

    while True:

        inner_html = get_parent()

        main_target = inner_html.findAll('div', {"class": "VkpGBb"})
        for _ in main_target:
            time.sleep(2)
            position_a = len(sheet.col_values(1)) + 1

            # Name
            child_target = _.find('div', {"class": "dbg0pd OSrXXb eDIkBe"})
            company_name = child_target.find('span').getText()
            k = company_name
            sheet.update_cell(position_a, 1, k)

            time.sleep(1)

            # Location
            child_target = _.find('div', {"class": "rllt__details"})
            divs = child_target.findAll('div')
            company_location = ""
            time.sleep(1)
            try:
                company_web = _.find('a', {"class": 'yYlJEf Q7PwXb L48Cpd'}).get('href')
                v = company_web
                sheet.update_cell(position_a, 2, v)
            except AttributeError:
                v = '-'
                sheet.update_cell(position_a, 2, v)
            time.sleep(2)

        try:
            time.sleep(3)
            browser.find_element_by_xpath('//*[@id="pnnext"]/span[2]').click()
        except NoSuchElementException:
            break


@app.get("/")
async def say_hello():
    return {"/search/<city>"}
