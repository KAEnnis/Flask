



from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/greet/")
@app.route("/greet/<a_name>")
def greet(a_name="anonymous"):
    return render_template("home.html", name=a_name) 


@app.route("/digitSum/<int:a_num>")                      
def digitSum(a_num):    
    sum = 0
    while (digit := a_num%10):
        sum += digit
        a_num = a_num//10

    return f"<h2> Sum or digits in URL num received is: {sum}<h2>"


if __name__ == '__main__':
    app.run(debug=True, port=8080)