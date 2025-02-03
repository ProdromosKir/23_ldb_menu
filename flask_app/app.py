import pandas as pd
from flask import Flask, render_template
from urllib.parse import quote
import os
from dotenv import load_dotenv




#-------

app = Flask(__name__)


google_sheet_url = os.getenv("GOOGLE_SHEET_URL")




class FoodItem:
    def __init__(self,food,value,url,category):
        self.food = food
        self.value = value
        self.url = url
        self.category = category
    def __repr__(self):
        return f"FoodItem(food='{self.food}', value={self.value}, url='{self.url}')"




@app.route('/')
def index():
    # Read the CSV data from the Google Sheet
    df = pd.read_csv(google_sheet_url)

    food_items = []

    for _, row in df.iterrows():
        food_item = FoodItem(food = row['Προιόν'], value=row['Τιμή'], url=row['URL'], category=row['Κατηγορία'])
        food_items.append(food_item)

    for item in food_items:
        print(item.food)

    return render_template('index.html', food_items=food_items)

if __name__ == "__main__":
    # Render provides the port as an environment variable
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)








