from bs4 import BeautifulSoup
import requests
from datetime import datetime
import os



url = 'https://valleyfoodsmed.com/weekly-ad/'

def get_html(url):
    response = requests.get(url)

    if response.status_code == 200:
        html_content = response.text
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

    return html_content


soup = BeautifulSoup(get_html(url), 'html.parser')

image_tags = soup.find_all('img')

image_urls = [img['src'] for img in image_tags]
ads = [image_urls[1], image_urls[2]]

now = datetime.now()
current_date = now.date()

counter = 0
for ad in ads:
    counter += 1
    response = requests.get(ad)
    
    if response.status_code == 200:
        folder_path = r'C:\Users\16196\Food Ads\valley_food_ads_'
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        
        filename = f'{current_date}_{counter}.jpg'
        file_path = os.path.join(folder_path, filename)
        
        with open(file_path, 'wb') as file:
            file.write(response.content)
        
        print('Image saved successfully.')
    else:
        print(f"Failed to retrieve the image. Status code: {response.status_code}")
