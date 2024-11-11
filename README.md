Food Price Finder

A Streamlit application that uses GPT-4 Vision to extract prices from grocery store advertisements.

Setup:

1. Clone the repository:
git clone https://github.com/yourusername/food-price-finder.git
cd food-price-finder

2. Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies:
pip install -r requirements.txt

4. Create a .env file in the root directory with your OpenAI API key:
OPENAI_API_KEY=your_api_key_here

5. Run the application:
streamlit run src/streamlit_ui.py

Project Structure:
- grab_ad: webscrapes the ads from each supermarket website
- ads: stores pictures of the ads
- food_mod: modifies the ads to crop each indivisual food item
- pictures: Stores images of the food items
- gray_pics: stores images of the grayscale food items (for better vision accuracy)
- gpt_call.py: Handles interaction with the GPT-4 Vision API
- streamlit_ui.py: Contains the Streamlit user interface

Contributing:
** Right now, this project only works for my local supermarkets, feel free to fork it for your own supermarkets**
1. Fork the repository
2. Create a new branch (git checkout -b feature/improvement)
3. Make changes and commit (git commit -am 'Add new feature')
4. Push to the branch (git push origin feature/improvement)
5. Create a Pull Request

Note: Make sure to keep your API key private and never commit it to the repository.
