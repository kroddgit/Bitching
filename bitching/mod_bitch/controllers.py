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

from flask_login import (
    current_user,
    login_required,
    login_user,
    logout_user,
)

from flask_wtf import (
    Form,
)

from bitching.mod_bitch.forms import (
    BitchForm
)
from bitching.mod_bitch.models import (
    Bitch
)

from bitching.mod_account.models import (
    User
)

from bitching import db

mod_bitch = Blueprint('bitch', __name__, url_prefix='/bitch')

@mod_bitch.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    form = BitchForm()
    if form.validate_on_submit():
        bitch = Bitch(current_user.id, form.bitch_input.data)
        db.session.add(bitch)
        db.session.commit()
        return redirect(url_for("bitch.home"))
    else:
        bitchList = Bitch.query.all()
        user = User.query.filter_by(id=current_user.id).first()
        return render_template('bitch/home.html', form=form, bitchList=bitchList, user=user)
