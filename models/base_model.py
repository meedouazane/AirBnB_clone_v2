#!/usr/bin/python3
"""
This module defines a base class for all models in our hbnb clone
"""
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from uuid import uuid4
from datetime import datetime
import models

Base = declarative_base()


class BaseModel:
    """
    A base class for all hbnb models
    """

    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ["created_at", "updated_at"]:
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        """Delete the current instance from the storage"""
        models.storage.delete(self)

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = dict(self.__dict__).copy()
        dictionary["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            dictionary[key] = value
            if key == "created_at" or key == "updated_at":
                dictionary[key] = value.isoformat()
        dictionary.pop("_sa_instance_state", None)
        return dictionary

    def __str__(self):
        """Returns a string representation of the instance"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )
