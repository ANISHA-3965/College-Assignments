from flask import Flask

app = Flask(__name__)

@app.route('/')
def student_details():
    return "Name: Anisha Vishwasrao<br>Roll Number: 101"

if __name__ == '__main__':
    app.run(debug=True)
    