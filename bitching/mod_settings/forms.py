from flask_wtf import (
    Form,
)
from wtforms import (
    TextField,
)

from wtforms_components import ColorField


class SettingsForm(Form):
    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False
        return True

    colorField = ColorField(
        'Favorite Color?',
    )
