from flask import Flask ,request, jsonify

app = Flask(__name__)

@app.route("/result", methods=["GET"])
def get_result():

    students = [
        {"name": "Anisha", "marks": 95, "result": "Pass"},
        {"name": "Vedant", "marks": 35, "result": "Fail"},
        {"name": "Joya", "marks": 68, "result": "Pass"}
    ]

    return jsonify(students)


@app.route("/addresult", methods=["POST"])
def add_result():

    data = request.get_json()

    name = data.get("name")
    marks = data.get("marks")

    if marks >= 40:
        result = "Pass"
    else:
        result = "Fail"

    return jsonify({
        "name": name,
        "marks": marks,
        "result": result
    })


if __name__ == "__main__":
    app.run(debug=True)
    