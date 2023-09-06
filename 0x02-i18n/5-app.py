#!/usr/bin/env python3
""" FLask APP"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """Config Class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_user():
    """Validate User"""
    id = request.args.get('login_in_as', None)
    if id is not None and int(id) in users.keys():
        return user.get(int(id))
    return None



@babel.localeselector
def get_locale():
    """Request languages"""
    user_req = request.args.get('locale')
    if user_req in app.config['LANGUAGES']:
        return user_req
    return request.accept_languages.best_match(app.config['LANGUAGES'])




@app.before_request
def before_request():
    """Get global user"""
    user = get_user()
    g.user = user

@app.route('/')
def index():
    """
    return renders
    html page
    """
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
