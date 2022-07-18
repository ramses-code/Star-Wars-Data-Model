import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    climate = Column(String(20))
    diameter = Column(Integer)

    def to_dict(self):
        return {}

class Vehicles(Base):
    __tablename__ = 'vehicles'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    passengers = (Integer)

    def to_dict(self):
        return{}

class Characters(Base):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    mass = Column(Integer)
    homeworld_id = Column(Integer, ForeignKey('planets.id'))
    planets = relationship(Planets)
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'))
    vehicles = relationship(Vehicles)

    def to_dict(self):
        return {}

class Fav_characters(Base):
    __tablename__ = 'fav_characters'

    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('characters.id'))
    characters = relationship(Characters)

    def to_dict(self):
        return{}

class Fav_planets(Base):
    __tablename__ = 'fav_planets'

    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer, ForeignKey('planets.id'))
    planets = relationship(Planets)
    
    def to_dict(self):
        return{}

class Fav_vehicles(Base):
    __tablename__ = 'fav_vehicles'

    id = Column(Integer, primary_key=True)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    vehicles = relationship(Vehicles)
    
    def to_dict(self):
        return{}


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')