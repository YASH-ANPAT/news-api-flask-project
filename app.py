from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("API_KEY")

@app.route("/", methods=["GET", "POST"])
def home():
    articles = []

    if request.method == "POST":
        query = request.form.get("query")

        url = f"https://newsapi.org/v2/everything?q={query}&apiKey={API_KEY}"
        response = requests.get(url)
        data = response.json()

        if data.get("status") == "ok":
            articles = data.get("articles", [])

    return render_template("index.html", articles=articles)

if __name__ == "__main__":
    app.run(debug=True)