from flask import Flask
import platform

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to System Information"

@app.route('/system')
def system_info():
    return f"""
    <h2>System Information</h2>
    <p>Operating System: {platform.system()}</p>
    <p>OS Version: {platform.version()}</p>
    <p>Machine: {platform.machine()}</p>
    <p>Processor: {platform.processor()}</p>
    """

if __name__ == '__main__':
    app.run(debug=True)
    