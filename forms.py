from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, BooleanField, validators

class NewPetForm(FlaskForm):
    """form for new and existing pets"""
    name = StringField("Pet name", [validators.InputRequired()])
    species = StringField(
        "Pet species", 
        [
            validators.InputRequired(), 
            validators.AnyOf(
                ['cat', 'dog', 'porcupine'], 
                message="Species must be cat, dog, or porcupine"
            )
        ]
    )
    photo_url = StringField(
        "Image URL", 
        [validators.URL(message="Please provide valid URL")
    ])
    age = IntegerField(
        "Pet age", 
        [validators.NumberRange(min=0, max=30, message="Age must be between 0 and 30")
    ])
    notes = TextAreaField("Notes")

class EditPetForm(FlaskForm):
    """form for editing pets"""
    photo_url = StringField("Image URL", [validators.URL(message="Please provide valid URL")])
    notes = TextAreaField("Notes")
    available = BooleanField("Available")
