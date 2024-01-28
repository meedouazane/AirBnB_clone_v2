#!/usr/bin/python3
"""
This module defines a class to manage file storage for hbnb clone
"""

import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls:
            cls_name = cls if isinstance(cls, str) else cls.__name__
            return {
                key: value
                for key, value in FileStorage.__objects.items()
                if key.split(".")[0] == cls_name
            }
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()["__class__"] + "." + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, "w") as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def delete(self, obj=None):
        """Deletes an object from the storage dictionary."""
        if obj is None:
            return
        key = obj.to_dict()["__class__"] + "." + obj.id
        if key in self.all():
            del self.all()[key]

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key in jo:
                self.__objects[key] = classes[jo[key]["__class__"]](**jo[key])
        except FileNotFoundError:
            pass

    def close(self):
        ''' deserializing the JSON file to objects '''
        self.reload()
