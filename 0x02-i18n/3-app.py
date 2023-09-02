#!/usr/bin/env python3
""" FLask APP"""
from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)


class Config(object):
    """Config Class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)

babel = Babel(app)


@app.route('/')
def index():
    """
    return renders
    html page
    """
    return render_template('1-index.html')


@babel.localeselector
def get_locale():
    """requests languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(host="0.0.0.0")
