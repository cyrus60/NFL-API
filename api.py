from flask import request, jsonify, Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello world"

app.run(debug=True, port=443)