#imports
from contextlib import nullcontext
import numbers
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.by import By

# chromedriver service initiation
service = Service('C:\Program Files (x86)\chromedriver.exe')
service.start()

# web driver definition
driver = webdriver.Remote(service.service_url)
driver.get('https://en.wikipedia.org/wiki/Telephone_numbers_in_Nigeria')

#try connecting to the element with classname wikitable
try:
    section= WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.CLASS_NAME,"wikitable"))
    )

    #connect to tbody tag in the section element
    table_data = section.find_elements(By.TAG_NAME,"tbody")
    numbers_array={}
    
    for i in table_data:
        now = i.text.split()
        for j in now:
            while j.isnumeric():
                nextelem = now[now.index(j)+1]
                if nextelem in numbers_array:
                    numbers_array[nextelem].append(j)
                else:
                    numbers_array[nextelem]=[]
                    numbers_array[nextelem].append(j)
    print(numbers_array)
            
finally:
    driver.quit()