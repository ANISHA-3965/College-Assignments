from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    current_datetime = datetime.now()
    return "Current Date and Time: " + str(current_datetime)

if __name__ == '__main__':
    app.run(debug=True)
    