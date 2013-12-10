"""
Setup and configure the Flask application.
"""
import sys
import logging

from flask import Flask
from flask.ext.bcrypt import Bcrypt
from flask.ext.login import LoginManager

from library import config

# Flask app, with a static folder:
app = Flask(__name__, static_folder='static', static_url_path='')

# Use the Flask config, but change things that show up in library.config:
app.config.update(config)

# Log to stdout:
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
app.logger.addHandler(handler)

# Setup Bcrypt
bcrypt = Bcrypt(app)

# Setup Flask-login:
from library.models.member import AnonymousMember, Member
from library.models import Session

login_manager = LoginManager()
login_manager.anonymous_user = AnonymousMember
login_manager.init_app(app)

@login_manager.user_loader
def load_user(member_id):
    """
    Gets the member for Flask-Login.
    """
    return Member.get(member_id)

# Tell jinja to clean whitespace:
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

# Setup teardown.
@app.teardown_appcontext
def shutdown_session(exception=None):
    """
    Cleans up after a request has been served.
    """
    if exception:
        ## This should include the request and the traceback as well:
        app.logger.error(str(exception))
    Session.remove()

# Load the views:
from library import views

if __name__ == "__main__":
    app.run()
