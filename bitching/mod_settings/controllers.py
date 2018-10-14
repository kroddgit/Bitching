import os
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
from sqlalchemy import update
from werkzeug import secure_filename

from flask_login import (
    current_user,
    login_required
)

from bitching.mod_settings.forms import (
    SettingsForm
)

from bitching.mod_account.models import (
    User
)

from bitching import (
    db,
    app,
    ALLOWED_EXTENSIONS
)
import json
import cloudinary
import cloudinary.uploader
from cloudinary.uploader import upload
import cloudinary.api

mod_settings = Blueprint('settings', __name__, url_prefix='/bitch')

@mod_settings.route('/settings', methods=['GET'])
@login_required
def settings():
    form = SettingsForm()
    if form.validate_on_submit():
        user = User.query.filter_by(id=current_user.id).first()
        db.session.commit()
        return redirect(url_for("settings.settings"))
    else:
        user = User.query.filter_by(id=current_user.id).first()
        return render_template('account/settings.html', form=form, user=user)

@mod_settings.route('/uploader', methods = ['POST'])
def upload_file():
   if request.method == 'POST':
       if 'file' not in request.files:
           flash("no file")
           return redirect(url_for("settings.settings"))
       file = request.files['file']
       if file.filename == '':
           flash("no selected file")
           return redirect(url_for("settings.settings"))
       if file and allowed_file(file.filename):
           upload_result = upload(file, public_id=current_user.id)
           print upload_result['url']
           user = User.query.filter_by(id=current_user.id).first()
           user.profilepicUrl = upload_result['url']
           db.session.commit()
           return redirect(url_for("settings.settings"))
       else:
           flash("Invalid image type!")
           return redirect(url_for("settings.settings"))
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
