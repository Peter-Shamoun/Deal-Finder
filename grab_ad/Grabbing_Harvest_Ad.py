from bs4 import BeautifulSoup
import requests
from datetime import datetime
import os
import time


now = datetime.now()
current_date = now.date()

image_url = 'http://harvestinternationalmarket.com/wp-content/uploads/WeeklyAd/HI_ElCajon_Ad.jpg'


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}


save_path = r'C:\Users\16196\Food Ads\harvest_ads_'
file_name = 'HI_ElCajon_Ad.jpg'
full_path = os.path.join(save_path, file_name)


response = requests.get(image_url, headers=headers)


if response.status_code == 200:
    os.makedirs(save_path, exist_ok=True)
    
    with open(full_path, 'wb') as file:
        file.write(response.content)
    print(f"Image successfully downloaded and saved to {full_path}.")
else:
    print(f"Failed to download the image. Status code: {response.status_code}")