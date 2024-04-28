from flask import Flask, render_template, url_for
from markupsafe import escape

wiki_links = {
    "Australia": "https://en.wikipedia.org/wiki/Australia",
    "Austria": "https://en.wikipedia.org/wiki/Austria",
    "Belgium": "https://en.wikipedia.org/wiki/Belgium",
    "Canada": "https://en.wikipedia.org/wiki/Canada",
    "China": "https://en.wikipedia.org/wiki/China",
    "Czechia": "https://en.wikipedia.org/wiki/Czechia",
    "Germany": "https://en.wikipedia.org/wiki/Germany",
    "Ireland": "https://en.wikipedia.org/wiki/Republic_of_Ireland",
    "Japan": "https://en.wikipedia.org/wiki/Japan",
    "Kazakhstan": "https://en.wikipedia.org/wiki/Kazakhstan",
    "Libya": "https://en.wikipedia.org/wiki/Libya",
    "Malaysia": "https://en.wikipedia.org/wiki/Malaysia",
    "Netherlands": "https://en.wikipedia.org/wiki/Netherlands",
    "Norway": "https://en.wikipedia.org/wiki/Norway",
    "Poland": "https://en.wikipedia.org/wiki/Poland",
    "Saudi Arabia": "https://en.wikipedia.org/wiki/Saudi_Arabia",
    "Singapore": "https://en.wikipedia.org/wiki/Singapore",
    "Turkmenistan": "https://en.wikipedia.org/wiki/Turkmenistan",
    "United Arab Emirates": "https://en.wikipedia.org/wiki/United_Arab_Emirates",
    "United States": "https://en.wikipedia.org/wiki/United_States"
}

app = Flask(__name__, template_folder="html_files")

# @app.route("/<name>")
# def hello(name):
#     return f"Hello, {escape(name)}!"

@app.route("/")
def index():
    return render_template("base.html")

@app.route("/view_instruct")
def view_instruct():
    return render_template("view_instruct.html")

@app.route("/main_illustration")
def main_illustration():
    return render_template("main_illustration.html")

@app.route("/countries")
def countries():
    return render_template("countries.html")

@app.route("/attributions")
def attributions():
    return render_template("attributions.html")

@app.route("/beautiful-web-type")
def beautifulwebtype():
    return render_template("beautiful-web-type")

@app.route("/country/<selected_country>")
def country(selected_country):
    wiki_link = wiki_links[selected_country]
    sidebar = get_wiki_sidebar(wiki_link)
    return render_template("country.html", country=selected_country, sidebar=sidebar, wiki_link=wiki_link)

# TESTING
from bs4 import BeautifulSoup
import requests

def get_wiki_sidebar(wiki_link):
    page = requests.get(wiki_link)
    soup = BeautifulSoup(page.content, 'html.parser')
    result = soup.find(class_="infobox ib-country vcard")
    if result is None:
        # Netherlands has a different class name
        result = soup.find(class_="infobox ib-pol-div vcard")

    html = str(result).replace('href="/wiki', 'href="https://en.wikipedia.org/wiki')
    return html


app.run(debug=True)