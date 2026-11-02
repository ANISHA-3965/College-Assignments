
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Course Information System!"

@app.route('/course/<course_name>')
def course(course_name):
    courses = {
        'python': 'Python is a programming language.',
        'java': 'Java is an object-oriented programming language.',
        'html': 'HTML is used to create web pages.',
        'css': 'CSS is used to style web pages.'
    }

    info = courses.get(course_name.lower(), 'Course information not found.')

    return f"<h1>Course: {course_name.upper()}</h1><p>{info}</p>"

if __name__ == '__main__':
    app.run(debug=True)
