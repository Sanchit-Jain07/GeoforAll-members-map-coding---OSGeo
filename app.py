from flask import Flask, jsonify, request, render_template
from univ import universities_scraper

app = Flask(__name__)


@app.route("/data", methods=["GET", "POST"])
def data():
    message = universities_scraper()
    return jsonify(message)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
