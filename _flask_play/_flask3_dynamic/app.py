from flask import Flask, render_template, redirect, session

app = Flask(__name__)
app.secret_key = "some unique real key this just for test"

@app.route("/")
@app.route("/home")
def home():
    print(session)
    a_name = session.get('name')  #no KeyError with get()
    if a_name:
        return render_template("home.html", name=a_name)
    
    return render_template("home.html")

@app.route("/greet/")
@app.route("/greet/<a_name>")
def greet(a_name="anonymous"):
    session['name'] = a_name         #add to the session dict
    return redirect('/home') 


@app.route("/contact")
def contact():
    return render_template("contact.html")                      



if __name__ == '__main__':
    app.run(debug=True, port=8080)
    