import pandas as pd
from flask import Flask, render_template



#-------

app = Flask(__name__)


# Replace this URL with the link to your Google Sheet (CSV format)
sheet_url = "https://docs.google.com/spreadsheets/d/1gYnWMG9MZigPiUTaWvz5NEC_S8Fb11HGhXmUmvOvG4g/pub?output=csv"

# Read the CSV data from the Google Sheet
df = pd.read_csv(sheet_url)

class FoodItem:
    def __init__(self,food,value,url,category):
        self.food = food
        self.value = value
        self.url = url
        self.category = category
    def __repr__(self):
        return f"FoodItem(food='{self.food}', value={self.value}, url='{self.url}')"


food_items = []

for _, row in df.iterrows():
    food_item = FoodItem(food = row['Προιόν'], value=row['Τιμή'], url=row['URL'], category=row['Κατηγορία'])
    food_items.append(food_item)

for item in food_items:
    print(item.food)


@app.route('/')
def index():
    return render_template('index.html', food_items=food_items)

if __name__ == '__main__':
    app.run(debug=True)







