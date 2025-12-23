import requests
from flask import Flask, render_template, jsonify
from dotenv import load_dotenv
import os

load_dotenv()
url = "https://api.api-ninjas.com/v1/quotes"
headers = {
    "X-Api-Key": os.getenv("API_KEY")
}

def get_quote():
    response = requests.get(url, headers=headers)
    data = response.json()
    if isinstance(data, list) and len(data) > 0:
        quote_value=data[0]['quote']
        author_value=data[0]['author']
        category_value=data[0]['category']
        return quote_value, author_value, category_value
    else:
        return "No quote found", "Unknown", "Unknown"

app = Flask(__name__)

@app.route('/')
def home():
    quote, author, category = get_quote()
    return render_template('ai_quote.html', quote1=quote, author1=author, category1=category)


if __name__ == '__main__':
    app.run(debug=True)