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
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            if "id" not in kwargs:
                kwargs["id"] = str(uuid4())
            if "created_at" not in kwargs:
                kwargs["created_at"] = str(datetime.now().isoformat())
            if "updated_at" not in kwargs:
                kwargs["updated_at"] = str(datetime.now().isoformat())
            kwargs["updated_at"] = datetime.strptime(
                kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f"
            )
            kwargs["created_at"] = datetime.strptime(
                kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f"
            )
            if "__class__" in kwargs:
                del kwargs["__class__"]
            for key, value in kwargs.items():
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
            self.__class__.__name__, self.id, self.to_dict()
        )
