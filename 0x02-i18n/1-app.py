#!/usr/bin/python3
""" FLask APP"""
from flask import Flask, render_template
from flask import Babel

app = Flask(__name__)
babel = Babel(app)

class Config:
    """Flask Config"""
    LANGAUGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


@app.route('/')
def index():
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0")
