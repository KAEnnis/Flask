from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    #See server output for `app.py` use of url_for() to attempt to ref static file
    print( url_for('static', filename='style.css') )
    return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True, port=8080)