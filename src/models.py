import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    favoritesId  = Column(Integer, ForeignKey('favorites.id'))
    userName = Column(String(25), unique=True)
    firstName = Column(String(30),nullable=False)
    lastName = Column(String(30),nullable=False)
    email = Column(String(40),unique=True, nullable=False)

class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    charactersId = Column (Integer, ForeignKey ('characters.id'))
    planetsId = Column (Integer, ForeignKey ('planets.id'))
    starshipsId = Column(Integer, ForeignKey ('starships.id'))
    vehiclesId = Column(Integer, ForeignKey ('vehicles.id'))

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(25))
    birthYear = Column(String(25))
    species = Column(String(25))
    height = Column(String(25))
    mass = Column(String(25))

class Planets (Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(25))
    population = Column(String(25))
    orbitalPeriod = Column(String(25))
    diameter = Column(String(25))
    gravity = Column(String(25))

class Starships(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    name = Column(String(25))
    model = Column(String(25))
    manufacturer = Column(String(25))
    speed = Column(String(25))

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(25))
    model = Column(String(25))
    manufacturer = Column(String(25))
    speed = Column(String(25))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
