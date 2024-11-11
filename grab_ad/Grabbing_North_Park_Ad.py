from bs4 import BeautifulSoup
import requests
from datetime import datetime
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

url = 'https://www.northparkproduce.com/copy-of-weekly-specials'

def get_html_with_scroll(url):
   
    driver = webdriver.Chrome() 
    driver.get(url)

    
    last_height = driver.execute_script("return document.body.scrollHeight")
    
    while True:
        
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        
        time.sleep(2) 
        
        
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    
    html_content = driver.page_source
    

    driver.quit()
    return html_content
html = get_html_with_scroll(url)


soup = BeautifulSoup(get_html_with_scroll(url), 'html.parser')

image_tags = soup.find_all('img')


image_urls = [img['src'] for img in image_tags]
ads = [image_urls[2], image_urls[-1]]



now = datetime.now()
current_date = now.date()

counter = 0
for ad in ads:
    counter += 1
    response = requests.get(ad)
    
    if response.status_code == 200:
        folder_path = r'C:\Users\16196\Food Ads\north_park_ads_'
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        
        filename = f'{current_date}_{counter}.jpg'
        file_path = os.path.join(folder_path, filename)
        
        with open(file_path, 'wb') as file:
            file.write(response.content)
        
        print('Image saved successfully.')
    else:
        print(f"Failed to retrieve the image. Status code: {response.status_code}")