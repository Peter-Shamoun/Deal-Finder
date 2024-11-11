from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Remove the hardcoded API key
API_KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = os.getenv('OPENAI_API_KEY')


import openai
import os
from openai import OpenAI
import base64
import requests
# import streamlit as st
from PIL import Image
import matplotlib as plt


def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')
  


def call():
    results = {}

    directory = r'C:\Users\16196\Food Ads\gray_valley_food_pics'

    for filename in os.listdir(directory):
        if filename[-1] != 's':
            gpt_file = r'C:\Users\16196\Food Ads\gray_valley_food_pics/'+filename
            base64_image = encode_image(rf'{gpt_file}')


            headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
            }
            
            
            payload = {
            "model": "gpt-4o",
            "messages": [
                {
                "role": "user",
                "content": [
                    {
                    "type": "text",
                    "text": """
                    
                        I am going to show you an image that contains various items. For each item, list its name, followed by a colon. 
                        After the colon, write the price of the item using the appropriate format. Use these guidelines for the price:
        
                        If the price is per weight, format it as '$X per lb' (or any relevant weight unit).
                        If the price is per unit, format it as '$X each.'
                        If there are any other formats (like 'per pack'), ensure the correct unit is represented.
                        Example:
                        
                        Apples: $2 per lb
                        Bottled Water: $1.50 each
                        Toilet Paper (12-pack): $10 per pack
                        Now, based on the image, please follow this format and provide the item names with prices. Do not include anything else other 
                        than the item and its price
                    
                    """
                    },
                    {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}"
                    }
                    }
                ]
                }
            ],
            "max_tokens": 300
            }
            
            response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
            text = response.json()['choices'][0]['message']['content']
            key = text.split(":")[0]
            val = text.split(":")[1]
            key_tup = (r'C:\Users\16196\Food Ads\valley_food_pics/'+filename , key)
            results[key_tup] = val
    return results


