#!/usr/bin/python3
""" Defines FileStorage that serializes instances to a
JSON file and deserialize JSON file to instances."""
import json
from base_model import BaseModel


class FileStorage:
    """Represents FileStorage engine for serializing/deserializing."""

    def __init__(self):
        """ Initializes a filestorage instance."""

        self.__file_path = "objects.json"
        self.__objects = {}

    def all(self):
        """Returns the dictionary __objects."""

        return self.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id."""

        key = "{}.{}".format(obj.__class__.__name__,obj.id)
        self.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file __file_path."""

    def reload(self):
        """ Deserializes the JSON file to __objects only if
        __file_path exists, otherwise do nothing.
        """

        pass
