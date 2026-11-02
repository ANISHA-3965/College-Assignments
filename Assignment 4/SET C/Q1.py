
from flask import Flask

app = Flask(__name__)

@app.route('/employee/<name>')
def employee(name):
    return f"Welcome, Employee {name}!"

if __name__ == '__main__':
    app.run(debug=True)
