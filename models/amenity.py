#!/usr/bin/python3
""" AMENITY MODLE"""
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base
import os


class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'
    name = Column(
        String(128), nullable=False
        ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
