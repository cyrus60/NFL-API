import flask 

app = flask.Flask(__name__)

@app.route('/', methods=["GET"])
def home():
    return "<h1>hello</h1>"

app.run()