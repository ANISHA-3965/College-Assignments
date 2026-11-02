from flask import Flask

app = Flask(__name__)

@app.route("/")
def product_list():

    products = [
        ("Laptop", 555000),
        ("Mobile", 255000),
        ("Tablet", 360000),
        ("Headphones", 559000),
        ("Smart Watch", 120000)
    ]

    expensive_product = products[0]

    for product in products:
        if product[1] > expensive_product[1]:
            expensive_product = product

    return f"""
    <h2>Most Expensive Product</h2>
    Product Name: {expensive_product[0]}<br>
    Price: ₹{expensive_product[1]}
    """

if __name__ == "__main__":
    app.run(debug=True)
    