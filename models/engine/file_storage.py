#!/usr/bin/env python3
"""File Storage Class."""
import json
import os


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

    def refresh(self):
        """Refresh objects to get new updates."""
        self.__objects[f"{self.obj.__class__.__name__}.{self.obj.id}"] = self.obj.to_dict()
        print(self.__objects)

    def new(self, obj):
        """Add new key to the Objects dict."""
        self.obj = obj
        self.refresh()

    def save(self):
        """Save Objects dict into json file."""
        self.refresh()
        self.jsons = json.dumps(self.__objects)
        self.jsonf = open(self.__file_path, 'w')
        print(self.jsons, file=self.jsonf)
        self.jsonf.close()

    def reload(self):
        """Re-Save Objects dict."""
        if os.path.exists(self.__file_path):
            self.jsonf = open(self.__file_path, 'r')
            self.__objects = json.load(self.jsonf)
            self.jsonf.close()
