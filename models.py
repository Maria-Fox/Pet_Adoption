from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def connect_db(app):
  '''Connect to database.'''
  
  db.app = app
  db.init_app(app)

class Pet(db.Model):  
  def __repr__(self):
    '''Show info about pet class'''

    p = self
    return f"<Pet id: {p.id}, Pet name: {p.pet_name}>, Pet species: {p.species},Photo url: {p.photo_url}, Pet age:{p.age}, Pet notes:{p.notes}> "


  __tablename__= "pets"

  id = db.Column(db.Integer, primary_key = True, autoincrement = True)
  pet_name = db.Column(db.Text, nullable = False)
  species = db.Column(db.Text, nullable= False)
  photo_url = db.Column(db.Text)
  age = db.Column(db.Integer)
  notes = db.Column(db.Text)
  available = db.Column(db.Boolean, default= True, nullable = False)

