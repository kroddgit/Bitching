from flask import (
    Blueprint,
    flash,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for
)

from werkzeug import (
    check_password_hash,
    generate_password_hash
)
from flask.ext.login import (
    current_user,
    login_required,
    login_user,
    logout_user,
)
mod_default = Blueprint('default', __name__)

@mod_default.route('/')
def home():
    return redirect(url_for("account.login"))
