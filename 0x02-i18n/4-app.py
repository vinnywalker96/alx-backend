#!/usr/bin/env python3
""" FLask APP"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """Config Class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Request languages"""
    user_req = request.args.get('locale')
    if user_req in app.config['LANGUAGES']:
        return user_req
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    return renders
    html page
    """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
