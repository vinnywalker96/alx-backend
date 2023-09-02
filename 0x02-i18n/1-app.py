#!/usr/bin/env python3
""" FLask APP"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel

class Config:
    """Flask Config"""
    LANGAUGES = ["en", "fr"]


app.config.from_object(Config)

babel.init_app(app, default_locale="en", default_timezone="UTC")


@app.route('/')
def index():
    """
    return renders
    html page
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0")
