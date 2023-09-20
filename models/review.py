#!/usr/bin/python3
""" REVIEW MODULE """
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
import os


class Review(BaseModel, Base):
    """REVIEW INFO CLASS."""
    __tablename__ = 'reviews'

    place_id = Column(
        String(60), ForeignKey('places.id'), nullable=False
        ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''

    user_id = Column(
        String(60), ForeignKey('users.id'), nullable=False
        ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    text = Column(
        String(1024), nullable=False
        ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
