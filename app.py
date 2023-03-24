from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to Python Flask Application - Mr. Raghu"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
