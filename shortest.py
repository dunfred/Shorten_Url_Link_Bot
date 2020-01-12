import requests
from urllib.request import urlopen
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
#import chromedriver_binary
driver_path = "/home/dunfred/webdrivers/chromedriver"

'''
driver = webdriver.Chrome(driver_path)

def scrape(url):
    driver.get(url)

    soup = BeautifulSoup(driver.page_source, "html5lib")
    last_index = int(driver.find_element_by_xpath('//*[@id="proxylisttable_paginate"]/ul/li[9]/a').text)

    for i in range(last_index):
        with open("ip.txt", "a") as ip:
            #[ip.write(i+"\n") for i in list(map(lambda x: x.text, soup.findAll("td")[::8])) if '.' in i]
            [ip.write(i+"\n") for i in list(map(lambda x: x[0]+":"+x[1], list(zip([i for i in list(map(lambda x: x.text, soup.findAll("td")[::8])) if '.' in i], 
                                                                             map(lambda x: x.text, soup.findAll('td')[1::8])))))]
            print(f'Page {i+1} loaded!')
            next_index = driver.find_element_by_xpath('//*[@id="proxylisttable_next"]/a').click()                                                    
            driver.implicitly_wait(20)
            soup = BeautifulSoup(driver.page_source, "html5lib")

#Site 1
url  = "https://free-proxy-list.net/"
scrape(url)

#Site 2
url = "https://www.sslproxies.org/"
scrape(url)

#Site 2
url = "https://www.us-proxy.org/"
scrape(url)
'''

short_links = ["http://festyy.com/wrIo7i", "https://corneey.com/we58lq", "https://clkmein.com/q9nTgz", "https://clkmein.com/q9nEQo", "http://gestyy.com/wyesSI",
               "http://clkmein.com/q9njAj", "http://clkmein.com/q9v2B2", "http://clkmein.com/q9zK1c", "http://clkmein.com/q9h3JB", "http://clkmein.com/q9h2Bn", 
               "http://clkmein.com/q9h1tI", "http://ceesty.com/wp3Uxo", "http://corneey.com/wieTgM", "http://corneey.com/wieRKS", "http://ceesty.com/wuJpxB", ]

with open("ip.txt", "r") as ip_address:        
    ip_list  = str(ip_address.read()).split("\n")
    chrome_options = webdriver.ChromeOptions()
    for proxy in ip_list:        
        print(proxy)                
        chrome_options.add_argument("--user-data-dir=/home/dunfred/.config/google-chrome/Default")
        chrome_options.add_argument('--proxy-server=%s' % proxy)            
        driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)
        driver.get('https://whatismyipaddress.com/') 
        driver.implicitly_wait(10)

''' for link in short_links:            
    try:            
        print(proxy)
        chrome_options.add_argument("--user-data-dir=/home/dunfred/.config/google-chrome/Default")
        chrome_options.add_argument('--proxy-server=%s' % proxy)            
        driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)
        print(link)
        driver.get(link)               
        driver.implicitly_wait(90)
        skip = driver.find_element_by_xpath('//*[@id="skip_button"]')
        skip.click()
        driver.explicitly_wait(10)
    except Exception:
        pass'''
'''

for link in short_links:           
    driver = webdriver.Chrome(driver_path)
    print(link)
    driver.get(link)               
    driver.implicitly_wait(30)
    skip = driver.find_element_by_xpath('//*[@id="skip_button"]')
    skip.click()
    driver.implicitly_wait(10)
'''
