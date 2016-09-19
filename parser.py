# -*- coding: utf-8 -*-
__author__ = 'sp41mer'
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome('/Users/sp41mer/PycharmProjects/FbPhoneSearch/chromedriver')

phones = [
    '89173470560',
    '89659426057',
    '89173579888',
    '89263332214',
    '89373055876',
    '89173788472',
    '89177674777',
    '89177581255',
    '89870580008',
    '89371600601',
    '89373200680',
    '89191592078',
    '89177546272',
    '89279390120',
    '89273130155',
    '89173478722',
    '89374907017',
    '79177818501',
    '89177539961',
    '89273333050',
    '89273338800'
]

urls = []

for phone in phones:
    driver.get("https://www.facebook.com/search/top/?q={}".format(phone))
    try:
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_css_selector('img'))
        html = driver.page_source
        soup = BeautifulSoup(html)
        url = soup.find('a', attrs={'class': '_fbBrowseXuiResult__profileImageLink'}).get('href')
        urls.append(url)
    except:
        print phone

print urls
