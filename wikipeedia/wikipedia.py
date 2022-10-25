#imports
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import json



#definition of variables
URL = "https://en.wikipedia.org/wiki/Telephone_numbers_in_Nigeria"


#start service and open the page
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get(URL)
driver.maximize_window()

#try connecting to the element with classname wikitable
array_numbers=[]
sim={"MTN":1,"Airtel":2,"Globacom":3,"Smile":4,"Multi-Links":5,"9Mobile":6,"Starcomms":7,"ZoomMobile":8,"Mtel":9}
try:
    section= WebDriverWait(driver,5).until(
        EC.presence_of_element_located((By.CLASS_NAME,"wikitable"))
    )

    #connect to tbody tag in the section element
    table_data = section.find_elements(By.TAG_NAME,"tbody")
  
    
    for i in table_data:

        numbers = i.text.split()
        for i in numbers:
            if i.isnumeric():
                next = numbers[numbers.index(i)+1]
                data={
                    "model":"sim_app.phonenumber",
                    "fields":{
                        "sim_network":sim[next],
                        "phone_number":i
                    }
                }
            array_numbers.append(data)
   
    # Serializing json

    
            
finally:
    if array_numbers:
        with open("data.json", "w") as json_obj:
            json.dump(array_numbers, json_obj)
    print("data created")
    driver.quit()