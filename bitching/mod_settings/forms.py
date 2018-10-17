from flask_wtf import (
    Form,
)
from wtforms import (
    TextField,
)


class SettingsForm(Form):
    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False
        return True
