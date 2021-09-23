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
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    lastname = Column(String(200), nullable=False)
    _password = Column(String(150), nullable=False)
    _mickname = Column(String(150), nullable = False)
    email = Column(String(150), nullable = False)

class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)

    id_user_fav = Column(Integer, ForeignKey('user.id'))
    user_ = relationship ('User')

    id_people_fav = Column(Integer, ForeignKey('people_view.id'))
    people = relationship('People_view')

    #id_planet_fav  = Column(Integer, ForeignKey('planet_view.id'))
    #id_planet_= relationship('Planet_view')
    
    id_starship_fav = Column(Integer, ForeignKey('starship_view.id'))
    id_starship = relationship('Starship_view')




class People_view(Base):
    __tablename__='people_view'
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

class Starship_view(Base):
    __tablename__='starship_view'
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

class Planet_view(Base):
    __tablename__='planet_view'
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



   
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')