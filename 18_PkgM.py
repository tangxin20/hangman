from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return "My name is tangxin."


app.run(port=8000)

