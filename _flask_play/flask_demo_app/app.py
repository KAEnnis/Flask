from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

products = {
   1:{
        "description": "Jeans",
        "price": 10.99,
        "amount": 5,
        "image_url": "https://plus.unsplash.com/premium_photo-1665664652383-2308d742943c?q=80&w=1964&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    },
    2:{
        "description": "Stylish Jeans",
        "price": 19.99,
        "amount": 10,
        "image_url": "https://images.unsplash.com/photo-1602293589930-45aad59ba3ab?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    },
    3:{
        "description": "Dress",
        "price": 15.50,
        "amount": 3,
        "image_url": "https://images.unsplash.com/photo-1595777457583-95e059d581b8?q=80&w=1983&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    }
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add-item",  methods=["GET"]) #now BOTH
def add_item_form():
    return render_template("form.html")

    
@app.route("/add-item",  methods=["POST"]) #now BOTH
def add_item_data():
    form_input = request.form.get("name") 
    product = {"description": form_input}
    index = len(products)+1
    products[index]= product        #add product
    return redirect(url_for("shop"))


@app.route("/order/<int:id>",  methods=["POST"])  
def order(id):
    print( request )
    product = products[id]
    if product["amount"] > 0:
        product["amount"] -= 1
        return product
    else:
        return "<h2>Out of Stock</h2>"

@app.route("/shop")
@app.route("/shop/<search_term>")
def shop(search_term=""):
    search_results=[]
    for product in products.values():
        if search_term in product["description"]:
            search_results.append(product)

    return render_template("shop.html", products=search_results)


if __name__ == '__main__':
    app.run(debug=True, port=8080)