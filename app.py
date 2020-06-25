from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import Pet, connect_db, db
from forms import NewPetForm, EditPetForm

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = "chickensarecool12341"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
toolbar = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def show_pets():
    """view func for root"""
    pets = Pet.query.all()
    return render_template('all_pets.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    """adds a new pet"""
    form = NewPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('add_pet.html', form=form)

@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def pet_details(pet_id):
    """see or edit pet details"""
    pet = Pet.query.get(pet_id)
    form = EditPetForm(obj=pet)
    if form.validate_on_submit():
        pet = Pet.query.get(pet_id)
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('pet_details.html', pet=pet, form=form)

