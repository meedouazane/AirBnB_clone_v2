"""
This module defines a class to manage database storage for hbnb clone
"""

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.user import User
from models.place import Place
from models.state import State
from models.review import Review


class DBStorage:
    """
    The DBStorage class
    """

    __engine = None
    __session = None

    def __init__(self):
        """"""
        self.__engine = create_engine(
            f"mysql+mysqldb://"
            + f"{getenv('HBNB_MYSQL_USER')}:{getenv('HBNB_MYSQL_PWD')}@"
            + f"{getenv('HBNB_MYSQL_HOST')}/{getenv('HBNB_MYSQL_DB')}",
            pool_pre_ping=True,
        )

    def all(self, cls=None):
        """"""
        dictionary = {}
        classes = [cls] if cls else [State, City]
        for cls in classes:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = f"{cls.__name__}.{obj.id}"
                dictionary[key] = obj
        return dictionary

    def new(self, obj):
        """"""
        self.__session.add(obj)

    def save(self):
        """"""
        self.__session.commit()

    def delete(self, obj=None):
        """"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """"""
        from models.city import City
        from models.state import State

        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)
