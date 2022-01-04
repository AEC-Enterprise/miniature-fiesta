from selenium import webdriver
import platform
from os import getcwd
from selenium.webdriver.chrome.service import Service

# ChromeDriver Setup
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--headless")
chrome_options.add_argument('--disable-notification')
chrome_options.add_argument('--disable-infobars')

if platform.system() == 'Windows':
    browser = webdriver.Chrome(getcwd() + '\chromedriver', options=chrome_options)
if platform.system() == 'Darwin' or platform.system() == 'Linux':
    browser = webdriver.Chrome(getcwd() + '/chromedriver', options=chrome_options)
