from flask import Flask, render_template, url_for
from markupsafe import escape

wiki_links = {
    "Australia": "https://en.wikipedia.org/wiki/Australia",
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
    return result


app.run(debug=True)