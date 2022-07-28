from dataclasses import dataclass
from flask import Flask, render_template, redirect, request, url_for
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import Pet_Form, EditPetForm

app = Flask(__name__)

app.debug = True
app.config['SECRET_KEY'] = 'secret-key'
toolbar = DebugToolbarExtension(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

# db connection & creation
connect_db(app)
db.create_all()

@app.route("/")
def visit_home():
    '''Displays all pets including name, photo if present, and pet availability.'''

    pets = Pet.query.all()
    print(pets)

    return render_template("home.html", pets = pets)

@app.route("/add", methods = ["GET", "POST"])
def add_pet_form():
  '''Form to add pet to db.'''

  form = Pet_Form()

# If CSRF token is valid & request is 'Post'
  if form.validate_on_submit():
      pet_name = form.pet_name.data
      species = form.species.data
      photo_url = form.photo_url.data
      age = form.age.data
      notes = form.notes.data

      new_pet = Pet(pet_name=pet_name, species = species, photo_url = photo_url, age= age, notes= notes)

      db.session.add(new_pet)
      db.session.commit()
      return redirect("/")

  else:
      return render_template("addPet.html", form = form)


@app.route("/<int:id>", methods= ["GET", "POST"])
def show_detail_edits(id):
  '''Display or edit given pet.'''

  pet = Pet.query.get_or_404(id)
  print(pet)
  # using the PetForm class and passing in the existing pet info
  form = EditPetForm(obj=pet)
  print(form)

  # Hits a post request & includes CSRF token
  if form.validate_on_submit():
    pet.photo_url = form.photo_url.data
    pet.notes = form.notes.data
    pet.available = form.available.data

    db.session.add(pet)
    db.session.commit(pet)

    return redirect("/")

  else:
    return render_template("details.html", pet = pet, form = form)




