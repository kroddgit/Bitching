from flask_wtf import (
    Form,
)
from wtforms import (
    StringField,
    PasswordField,
    RadioField,
    TextAreaField,
    TextField,
    validators,
)

class LoginForm(Form):
    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False
        return True

    user_name = StringField(
        'username:'
    )
    password = PasswordField(
        'Password:'
    )

class RegisterForm(Form):
    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False
        return True

    username = StringField(
        'username:'
    )
    email = StringField(
        'email:'
    )
    password = PasswordField(
        'Password:'
    )
    retype = PasswordField(
        'Password Retype:'
    )

class SettingsForm(Form):
    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False
        return True

    username = StringField(
        'username:'
    )
    email = StringField(
        'email:'
    )
    password = PasswordField(
        'Password:'
    )
    retype = PasswordField(
        'Password Retype:'
    )
