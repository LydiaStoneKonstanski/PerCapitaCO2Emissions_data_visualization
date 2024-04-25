from flask import Flask, render_template
from markupsafe import escape

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


app.run(debug=True)