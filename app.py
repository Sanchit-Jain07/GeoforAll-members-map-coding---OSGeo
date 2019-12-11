from flask import Flask, jsonify, request, render_template
from univ import universities_scraper

app = Flask(__name__)


@app.route("/data", methods=["GET", "POST"])
def index():
    message = universities_scraper()
    return jsonify(message)


@app.route("/test")
def test_page():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
