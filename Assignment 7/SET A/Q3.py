from flask import Flask,jsonify
app = Flask(__name__)
products=[
    {"name" : "Mouse", "price" : 1500, "category" : "electronic"},
    {"name" : "Laptop", "price" : 62000 , "category" : "electronic"}
]

@app.route('/product',methods=['GET'])
def product_details():
    return jsonify(products)

if __name__=='__main__':
    app.run(debug=True)
    