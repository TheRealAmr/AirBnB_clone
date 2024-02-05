#!/usr/bin/python3
"""Base Model Class."""
from uuid import uuid4
import datetime


class BaseModel:
    """base class.

    Attributes:
        __size (int): square size
    """

    def __init__(self):
        """Initialize the square instance."""
        self.id = str(uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """Return String represent."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update date."""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Return a dict."""
        dict = self.__dict__.copy()
        dict['__class__'] = self.__class__.__name__
        dict['created_at'] = self.created_at.isoformat()
        dict['updated_at'] = self.updated_at.isoformat()
        return dict
