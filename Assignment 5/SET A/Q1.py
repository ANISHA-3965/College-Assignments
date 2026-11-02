from flask import Flask,request
app = Flask(__name__)

@app.route('/')
def student():
    
    name = request.args.get('name')
    return f"student name : {name}"

if __name__ == '__main__':
    app.run(debug=True)
    