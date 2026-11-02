from flask import Flask,request,jsonify
app = Flask(__name__)

products=[
    {"name":"Laptop", "Price": 62000, "Category":"Electronic"},
    {"name":"Mobile", "Price": 50000, "Category":"Electronic"},
    {"name":"Mouse", "Price": 2000, "Category":"Electronic"},
]

@app.route('/product',methods=['GET'])
def product_details():
    return jsonify(products)
        
@app.route('/addproduct',methods=['POST'])
def add_product():
    
    data = request.get_json()

    name = data.get("name")
    price = data.get("price")

    product = {
        "name":name,
        "price":price
    }

    products.append(product)

    return jsonify(
        {
            "msg":"Product added sucessfully",
            "product":product
        }
    ),201
    
if __name__ == '__main__':
    app.run(debug = True)

