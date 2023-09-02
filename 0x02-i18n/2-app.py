#!/usr/bin/python3
""" FLask APP"""
from flask import Flask, render_template
from flask_babel import Babel, request

app = Flask(__name__)
babel = Babel(app)

class Config:
    """Flask Config"""
    LANGAUGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)


@babel.localeselector
def get_locale():
    locale = request.accept_languages.best_match(
            app.config['LANGUAGES'])
    return locale


@app.route('/')
def index():
    return render_template('2-index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0")
