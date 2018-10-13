# System imports
import os
import sys
import cloudinary
import cloudinary.uploader
from cloudinary.uploader import upload
import cloudinary.api
from cloudinary.utils import cloudinary_url
# Flask imports
from flask import Flask, render_template, flash
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

from flask_login import (
    LoginManager,
    current_user,
    login_user,
    logout_user,
)
from flask_uploads import (
    configure_uploads,
    IMAGES,
    UploadSet,
)
from flask_wtf import (
    CsrfProtect,
)

IMAGE_SET = UploadSet('images', IMAGES)

# Define the web app
sys.stdout.write('Creating Flask app...')
app = Flask(__name__)
sys.stdout.write('Done\n')

# Enable CSRF Protection
sys.stdout.write('Enabling CSRF Protection...')
CsrfProtect(app)
sys.stdout.write('Done\n')

# Define the database
sys.stdout.write('Defining SQLAlchemy database...')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bitching.db'
db = SQLAlchemy(app)
sys.stdout.write('Done\n')

# Create the login manager
sys.stdout.write('Creating login manager...')
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "/bitch/login"
sys.stdout.write('Done\n')

# Register Mailer service
sys.stdout.write('Configuring Mailer service...')
mail = Mail(app)
sys.stdout.write('Done\n')


# Register error handlers
sys.stdout.write('Registering error handlers...')
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def flash_form_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(
                "%s: %s" % (getattr(form, field).label.text, error),
                "alert-danger"
            )
sys.stdout.write('Done\n')

# Import all blueprints from controllers
from bitching.controllers import mod_default
from bitching.mod_account.controllers import mod_account
from bitching.mod_bitch.controllers import mod_bitch
from bitching.mod_settings.controllers import mod_settings


# Register blueprints
sys.stdout.write('Registering blueprint modules...')
app.register_blueprint(mod_default)
app.register_blueprint(mod_account)
app.register_blueprint(mod_bitch)
app.register_blueprint(mod_settings)

sys.stdout.write('Done\n')

sys.stdout.write('\nApp done loading.\n')
app.secret_key="kgrodd"

cloud = cloudinary.config.update = ({
    'df7hg9q6i',
    '639662597519516',
    'cC2ak5GbxVWkbr9qg4UphZOBrw4'
})
cloudinary.config(cloud_name='df7hg9q6i', api_key='639662597519516',
                  api_secret='cC2ak5GbxVWkbr9qg4UphZOBrw4')
