from selenium import webdriver
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from selenium.webdriver.chrome.service import Service
import pprint
from bs4 import BeautifulSoup

# --------------------------------------------------------------------------------------
# Chrome settings:
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--headless")
chrome_options.add_argument('--disable-notification')
chrome_options.add_argument('--disable-infobars')
browser = webdriver.Chrome('./chromedriver', options=chrome_options)
# --------------------------------------------------------------------------------------
# SHEET SETUP
scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name('static/key/api.json', scope)
client = gspread.authorize(credentials)
sheet = client.open_by_key("1jGMF0OBt8x20C8eLX9u6Qx8sADyy870kLyxE0HO_U2g").sheet1
# --------------------------------------------------------------------------------------
    
    
def click_xpath(xpath):
    browser.find_element_by_xpath(xpath).click()


def wait_till(time):
    browser.implicitly_wait(time)


search = "Software Companies in Kakinada"

wait_till(20)
browser.get('https://google.com/search?q=' + search)

wait_till(20)
click_xpath('//*[@id="Odp5De"]/div/div/div/div[2]/div[1]/div[2]/g-more-link/a/div')

names = []

for n in range(11, 29):
    try:
        wait_till(20)
        names.append(browser.find_element_by_xpath(f'//*[@id="tsuid{n}"]/div/div/a[1]/div/div[1]/span').text)
    except:
        pass

print(names)
browser.quit()
