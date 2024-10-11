from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class SummarizeText(FlaskForm):
    text = StringField(label = 'Input Your Text Here: ', validators = [Length(min=20), DataRequired()])
    submit = SubmitField(label='Summarize Text')