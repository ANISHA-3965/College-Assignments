from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)


def get_connection():
    con = psycopg2.connect(
        database="systemdb",
        user="postgres",
        password="Dorit",
        host="localhost",
        port="5432"
    )
    return con

def create_table():
    con = get_connection()
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS student (
            student_id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            course VARCHAR(100) NOT NULL
        )
    """)

    con.commit()
    cur.close()
    con.close()

@app.route("/")
def home():
    con = get_connection()
    cur = con.cursor()

    cur.execute("SELECT * FROM student ORDER BY student_id")
    students = cur.fetchall()

    cur.close()
    con.close()

    return render_template("index.html", students=students)

@app.route("/add", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        name = request.form["name"].strip()
        course = request.form["course"].strip()

        if not name or not course:
            return "Name and course are required.", 400

        con = get_connection()
        cur = con.cursor()

        cur.execute(
            "INSERT INTO student (name, course) VALUES (%s, %s)",
            (name, course)
        )

        con.commit()
        cur.close()
        con.close()

        return redirect("/")

    return render_template("add.html")

@app.route("/update/<int:student_id>", methods=["GET", "POST"])
def update_student(student_id):
    con = get_connection()
    cur = con.cursor()

    if request.method == "POST":
        name = request.form["name"].strip()
        course = request.form["course"].strip()

        if not name or not course:
            cur.close()
            con.close()
            return "Name and course are required.", 400

        cur.execute(
            """UPDATE student
               SET name = %s, course = %s
               WHERE student_id = %s""",
            (name, course, student_id)
        )

        con.commit()
        cur.close()
        con.close()

        return redirect("/")

    cur.execute(
        "SELECT * FROM student WHERE student_id = %s",
        (student_id,)
    )

    student = cur.fetchone()

    cur.close()
    con.close()

    if student is None:
        return "Student not found.", 404

    return render_template("update.html", student=student)

@app.route("/delete/<int:student_id>", methods=["POST"])
def delete_student(student_id):
    con = get_connection()
    cur = con.cursor()

    cur.execute(
        "DELETE FROM student WHERE student_id = %s",
        (student_id,)
    )

    con.commit()
    cur.close()
    con.close()

    return redirect("/")


if __name__ == "__main__":
    create_table()
    app.run(debug=True)
    