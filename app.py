"""The main application."""


from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello():
    """Say hello."""
    return "Hello, World!"


@app.route('/<name>')
def hello_name(name):
    """Say hello to someone's name."""
    return "Hello, {}".format(name)


if __name__ == "__main__":
    app.run()
