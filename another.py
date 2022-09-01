
from unicodedata import name
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service('C:\Program Files (x86)\chromedriver.exe')

service.start()

driver = webdriver.Remote(service.service_url)

driver.get('https://awajis.com/all-nigerian-gsm-numbers-and-networks/')

#  checking the number and printing 






try:
    section = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.TAG_NAME, "table"))
    )
    table_rows = section.find_elements(By.TAG_NAME,'tr')
    sim_array=['MTN','GLO','AIRTEL','VISAFONE','9MOBILE','VISAFONE']
    numbers_array=[]

    for i in table_rows:
        table_data = i.find_elements(By.TAG_NAME,'td')
        names=table_data[-1].text
        number=table_data[0].text

        if names in sim_array :
            numbers_array.append([names,number])
    
finally:
    driver.quit()