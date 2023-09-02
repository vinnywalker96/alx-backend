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

def get_user():
    users = {
             1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
             2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
             3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
             4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
    }
    login = request.args.get('login_as')
    if login in  users:
        return users[login]
    return None


@app.before_request
def before_request():
    return

@app.route('/')
def index():
    return render_template('5-index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
