from flask import Flask, render_template

app = Flask(__name__)


@app.route("/home")
def index():
    return render_template("index.html")


@app.route("/canyon")
def canyon():
    return render_template("canyon.html")


@app.route("/javelina")
def javelina():
    return render_template("javelina.html")


@app.route("/weekend")
def weekend():
    return render_template("weekend.html")


@app.route("/festival")
def festival():
    return render_template("festival.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=8080)
