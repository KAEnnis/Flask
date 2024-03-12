from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def tiddlywinks():
    return "<h1>Hello</h1><p>Text inside</p>"

if __name__ == '__main__':
    app.run(debug=True, port=8080)