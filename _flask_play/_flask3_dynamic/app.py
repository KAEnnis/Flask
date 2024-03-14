from flask import Flask, render_template, redirect, session, url_for

app = Flask(__name__)
app.secret_key = "some unique real key this just for test"

@app.route("/")
@app.route("/home")
def index():
    print(session)
    a_name = session.get('name')    
    if a_name:
        return render_template("index.html", name=a_name)
    
    return render_template("index.html")

@app.route("/greet/")
@app.route("/greet/<a_name>")
def greet(a_name="anonymous"):
    session['name'] = a_name         
    return redirect('/home') 


@app.route("/contact")
def contact_me():
    print( url_for('index')  )
    return render_template("contact.html")                      



if __name__ == '__main__':
    app.run(debug=True, port=8080)
    