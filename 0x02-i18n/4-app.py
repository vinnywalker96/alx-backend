#!/usr/bin/python3
""" FLask APP"""
from flask import Flask, render_template
from flask import request
from flask_babel import Babel, request, _

app = Flask(__name__)



class Config(object):
    """Flask Config"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)
babel = Babel(app)

@babel.localeselector
def get_locale():
    user_locale = request.args.get('locale')
    return user_locale



@app.route('/')
def index():
    return render_template('4-index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
