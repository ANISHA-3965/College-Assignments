from flask import Flask
app = Flask(__name__)

@app.route('/contact')
def contact():
    return "Contact Us"

@app.route('/service')
def service():
    return "Welcome to Our Services Page! We provide reliable and efficient services to meet your needs."

if __name__ =='__main__':
    app.run(debug=True)
    
