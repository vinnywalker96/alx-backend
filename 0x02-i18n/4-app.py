#!/usr/bin/env python3
""" FLask APP"""
from flask import Flask, render_template, request
from flask_babel import Babel, _, get_locale

app = Flask(__name__)


class Config(object):
    """Config Class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    """Request languages"""
    if request.args.get('locale') in app.config['LANGUAGES']:
        return request.args.get('locale')
    return 

@app.route('/')
def index():
    """
    return renders
    html page
    """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
