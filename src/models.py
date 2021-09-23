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
    id = Column(Integer, primary_key=True)
    _password = Column(String(150), nullable=False)
    _nickname = Column(String(150), nullable = False)
    name = Column(String(100), nullable=False)
    lastname = Column(String(200), nullable=False)
    email = Column(String(150), nullable = False)

    have_favorites = relationship("Favorites", backref="user")

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    people_id = Column(Integer, ForeignKey('people.id'))
    starship_id = Colum(Integer, ForeignKey("starship.id"))
    planet_id = Colum(Integer, ForeignKey("planet.id"))

class People(Base):
    __tablename__='people'
    id = Column (Integer, primary_key = True)
    url = Column (String, nullable= True )  
    name = Column(String(150), nullable = True)
    height = Column(Integer, nullable= False)
    mass = Column(Integer, nullable=False)
    hair_color = Column(String(50), nullable=False)
    skin_color = Column(String(50), nullable = False)
    eyes_color = Column(String(50), nullable = False)
    birth_year = Column(Date,nullable = False)
    created  = Column(String, nullable = False)
    edited = Column(String, nullable = False)
    homeworld = Column(String, nullable = True)

    have_favorites = relationship("Favorites", backref="people")

class Starship(Base):
    __tablename__='starship'
    id = Column(Integer, primary_key = True)
    url = Column(String, nullable=False)
    name = Column(String, nullable = True )
    model = Column(String, nullable = False)
    straship_ = Column(String, nullable = False)
    manufacture = Column(String, nullable = False)
    incredit = Column(String, nullable = False )
    lenght = Column(String, nullable = False)
    grew = Column(String, nullable = False)
    passenger = Column(String, nullable = False)
    max_atmospheric_speed = Column(String, nullable = False)
    hyperdrive_rating = Column(String, nullable = False)
    mglt = Column(String, nullable = False)
    cargo_capacity = Column(String, nullable = False)
    consumables = Column(String, nullable = False)
    pilot = Column(String, nullable = False)
    edited = Column(String, nullable = False)
    created = Column(String, nullable = False)

    have_favorites = relationship("Favorites", backref="starhip")

class Planet(Base):
    __tablename__='planet'
    id = Column(Integer, primary_key = True)
    url = Column(String, nullable = True )
    name =  Column(String, nullable = True )
    diameter = Column(Integer, nullable = False)
    rotation_period = Column(String, nullable = False)
    orbital_period = Column(String, nullable = False)
    gravity = Column(String, nullable = False)
    population = Column(String, nullable = False)
    climate = Column(String, nullable = False)
    terrain = Column(String, nullable = False)
    surface_water = Column(String, nullable = False)
    create = Column(String, nullable = False)
    edited = Column(String, nullable = False)
    description = Column(String, nullable = False)

    have_favorites = relationship("Favorites", backref="planet")

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')