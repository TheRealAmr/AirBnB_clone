#!/usr/bin/python3
"""Base Model Class."""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """base class.

    Attributes:
        kwargs: any passed args for Json to class
    """

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel instance."""
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'updated_at' or key == 'created_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)

    def __str__(self):
        """Return String represent."""
        return self.__class__.__name__

    def save(self):
        """Update date."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dict."""
        dict = self.__dict__.copy()
        dict['__class__'] = self.__class__.__name__
        dict['created_at'] = self.created_at.isoformat()
        dict['updated_at'] = self.updated_at.isoformat()
        return dict
