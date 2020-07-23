"""The main application."""


from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello():
    """Say hello."""
    return "Hello, World!"


if __name__ == "__main__":
    app.run()
