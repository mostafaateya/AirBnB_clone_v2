#!/usr/bin/python3
""" STATE MODULE """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel
from models.city import City
import models


class State(BaseModel, Base):
    """ CLASS STATE """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='all, delete')

    @property
    def cities(self):
        """
        LIST OF CITY
        """

        records = models.storage.all()
        res = []
        for city in records.values():
            if self.id == city.state_id:
                res.append(city)
        return res

    if models.storage_t != "db":
        @property
        def cities(self):
            """getter for list of city instances related to the state"""
            city_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
