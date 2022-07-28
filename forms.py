from secrets import choice
from wsgiref.validate import validator
from xmlrpc.client import Boolean
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, URLField, BooleanField, TextAreaField
from wtforms.validators import InputRequired, Optional, Email, URL, Length, NumberRange

# passing in the FlaskForm instance to each class
class Pet_Form(FlaskForm):
  '''Form for adding a new pet'''

# filed for completion = type of field (rendered to client)
  pet_name = StringField("Pet Name", validators = [InputRequired()])

  species = SelectField("Species", choices =[('Cat', "Cat"), ("Dog", "Dog"), ("p_pine", "Porcupine")], validators = [InputRequired()])

  photo_url = URLField("Photo URL", validators =[Optional(), URL()])

  age = IntegerField("Age", validators = [Optional(), NumberRange(min = 0, max = 30, message = "Valid age is between 0 and 30.")])

  notes = TextAreaField("Notes", validators=[Optional(), Length(min = 5)])
  
  available = BooleanField("Pet availability", validators = [InputRequired()])


class EditPetForm(FlaskForm):
    """Form to edit an existing pet."""

    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()],
    )

    notes = TextAreaField(
        "Comments",
        validators=[Optional(), Length(min=10)],
    )

    available = BooleanField("Available")