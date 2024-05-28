#!/usr/bin/env python3
"""Flask application"""

from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)


class Config:
    """configures a flask app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'fr'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/', strict_slashes=False)
def index():
    """Landing page"""
    return render_template("1-index.html")


@babel.localeselector
def get_locale():
    """Determines best match with our supported languages"""

    req = request.args.get('locale')

    if req and req in app.config['LANGUAGES']:
        return req
        
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(debug=True)
