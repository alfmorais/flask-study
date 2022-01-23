from flask import Flask

app = Flask(__name__)

@app.route("/")  # example: https://google.com.br/
def home():
    return "Hello, world!"


app.run(port=5000)
