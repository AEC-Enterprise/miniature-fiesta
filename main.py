from driver_Setup import browser
from sheet_setup import sheet


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
