"""
This module defines a class to manage database storage for hbnb clone
"""

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """
    The DBStorage class
    """

    __engine = None
    __session = None

    def __init__(self):
        """Initialize the DBStorage class."""
        self.__engine = create_engine(
            f"mysql+mysqldb://"
            + f"{getenv('HBNB_MYSQL_USER')}:{getenv('HBNB_MYSQL_PWD')}@"
            + f"{getenv('HBNB_MYSQL_HOST')}/{getenv('HBNB_MYSQL_DB')}",
            pool_pre_ping=True,
        )

    def all(self, cls=None):
        """Returns a dictionary of models currently in the database"""
        dictionary = {}
        classes = [cls] if cls else [State, City, User, Place, Review, Amenity]
        for cls in classes:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = f"{cls.__name__}.{obj.id}"
                dictionary[key] = obj
        return dictionary

    def new(self, obj):
        """Adds new object to the database"""
        self.__session.add(obj)

    def save(self):
        """Saves to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes object from the database"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Loads objects from the databas"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)
