#!/usr/bin/python3
""" Defines FileStorage that serializes instances to a
JSON file and deserialize JSON file to instances."""
import json
from models.base_model import BaseModel


class FileStorage:
    """Represents FileStorage engine for serializing/deserializing."""

    
