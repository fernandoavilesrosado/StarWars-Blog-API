import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    _password = db.Column(db.String(150), nullable=False)
    _nickname = db.Column(db.String(150), nullable = False)
    name = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(150), nullable = False)

    have_favorites = relationship("Favorites", backref="user")

class Favorites(Base):
    __tablename__ = 'favorites'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    people_id = db.Column(db.Integer, ForeignKey('people.id'))
    starship_id = db.Colum(db.Integer, ForeignKey("starship.id"))
    planet_id = db.Colum(db.Integer, ForeignKey("planet.id"))

class People(Base):
    __tablename__='people'
    id = db.Column (db.Integer, primary_key = True)
    url = db.Column (db.String, nullable= True )  
    name = db.Column(db.String(150), nullable = True)
    height = db.Column(db.Integer, nullable= False)
    mass = db.Column(db.Integer, nullable=False)
    hair_color = db.Column(db.String(50), nullable=False)
    skin_color = db.Column(db.String(50), nullable = False)
    eyes_color = db.Column(db.String(50), nullable = False)
    birth_year = db.Column(db.Date,nullable = False)
    created  = db.Column(db.String, nullable = False)
    edited = db.Column(db.String, nullable = False)
    homeworld = db.Column(db.String, nullable = True)

    have_favorites = relationship("Favorites", backref="people")

class Starship(Base):
    __tablename__='starship'
    id = db.Column(db.Integer, primary_key = True)
    url = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable = True )
    model = db.Column(db.String, nullable = False)
    straship_ = db.Column(db.String, nullable = False)
    manufacture = db.Column(db.String, nullable = False)
    incredit = db.Column(db.String, nullable = False )
    lenght = db.Column(db.String, nullable = False)
    grew = db.Column(db.String, nullable = False)
    passenger = db.Column(db.String, nullable = False)
    max_atmospheric_speed = db.Column(db.String, nullable = False)
    hyperdrive_rating = db.Column(db.String, nullable = False)
    mglt = db.Column(db.String, nullable = False)
    cargo_capacity = db.Column(db.String, nullable = False)
    consumables = db.Column(db.String, nullable = False)
    pilot = db.Column(db.String, nullable = False)
    edited = db.Column(db.String, nullable = False)
    created = db.Column(db.String, nullable = False)

    have_favorites = relationship("Favorites", backref="starhip")

class Planet(Base):
    __tablename__='planet'
    id = db.Column(db.Integer, primary_key = True)
    url = db.Column(db.String, nullable = True )
    name =  db.Column(db.String, nullable = True )
    diameter = db.Column(db.Integer, nullable = False)
    rotation_period = db.Column(db.String, nullable = False)
    orbital_period = db.Column(db.String, nullable = False)
    gravity = db.Column(db.String, nullable = False)
    population = db.Column(db.String, nullable = False)
    climate = db.Column(db.String, nullable = False)
    terrain = db.Column(db.String, nullable = False)
    surface_water = db.Column(db.String, nullable = False)
    create = db.Column(db.String, nullable = False)
    edited = db.Column(db.String, nullable = False)
    description = db.Column(db.String, nullable = False)

    have_favorites = relationship("Favorites", backref="planet")

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')