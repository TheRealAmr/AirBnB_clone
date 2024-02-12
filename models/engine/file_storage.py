#!/usr/bin/env python3
"""File Storage Class."""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.review import Review
from models.place import Place
from models.city import City
from models.amenity import Amenity


class FileStorage:
    """file store class.

    Attributes:
        kwargs: any passed args for Json to class
    """

    def __init__(self, *args, **kwargs):
        """Initialize FileStore instance.

        File path defined twice One private (task requirement)
        and One public for unittest
        """
        self.__file_path = "file.json"
        self.file_path = self.__file_path
        self.__objects = {}

    def all(self):
        """Return Objects dict."""
        return self.__objects

    def new(self, obj):
        """Add new key to the Objects dict."""
        self.__objects[
            f"{obj.__class__.__name__}.{obj.id}"
            ] = obj

    def save(self):
        """Save Objects dict into json file."""
        js = {}
        for key, value in self.__objects.items():
            js[key] = value.to_dict()
        self.jsons = json.dumps(js)
        self.jsonf = open(self.__file_path, 'w')
        print(self.jsons, file=self.jsonf)
        self.jsonf.close()

    def reload(self):
        """Re-Save Objects dict."""
        if os.path.exists(self.__file_path):
            self.jsonf = open(self.__file_path, 'r')
            self.d = json.load(self.jsonf)
            for key, obj in self.d.items():
                newObj = eval(obj['__class__'])(**obj)
                self.__objects[key] = newObj
            self.jsonf.close()
