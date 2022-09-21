#imports
from contextlib import nullcontext
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#definition of variables
URL = "https://en.wikipedia.org/wiki/Telephone_numbers_in_Nigeria"
PATH = "C:\chromedriver.exe"

#start service and open the page
service= Service(PATH)
service.start()
driver = webdriver.Remote(service.service_url)
driver.get(URL)


#try connecting to the element with classname wikitable
try:
    section= WebDriverWait(driver,5).until(
        EC.presence_of_element_located((By.CLASS_NAME,"wikitable"))
    )

    #connect to tbody tag in the section element
    table_data = section.find_elements(By.TAG_NAME,"tbody")
    array_numbers={}
    
    for i in table_data:

        numbers = i.text.split()
        for i in numbers:
            if i.isnumeric():
                next = numbers[numbers.index(i)+1]
                if next in array_numbers:
                    array_numbers[next].append(i)
                else:
                    array_numbers[next]=[] 
                    array_numbers[next].append(i)

    print(array_numbers)
    
            
finally:
    driver.quit()