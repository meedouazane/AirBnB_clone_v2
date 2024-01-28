#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from os import getenv


class State(BaseModel, Base):
    """
    The State class
    """

    __tablename__ = "states"

    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)

        cities = relationship(
            "City",
            backref="state",
            cascade="all, delete-orphan",
        )
    else:
        name = ""

        @property
        def cities(self):
            """Returns the list of City instances with
            state_id equals to the current State.id"""
            from models import storage
            from models.city import City

            all_cities = storage.all(City)
            return [
                city
                for city in all_cities.values()
                if city.state_id == self.id
            ]
