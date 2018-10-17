from flask_wtf import (
    Form,
)
from wtforms import (
    PasswordField,
    RadioField,
    TextAreaField,
    TextField,
    validators,
)

class BitchForm(Form):
    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        
    def validate(self):
        if not Form.validate(self):
            return False
        return True

    bitch_input = TextAreaField(
        'Bitch about something!',
    )
