#!/usr/bin/python3
"""File storage class"""
import datetime
import os
import json


class FileStorage:

    """class for storing and retrieving data"""
    __filepath = "file.json"
    __objects = {}

    def all(self):
        """retunr dctionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            x = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(x, f)

    def reload(self):
        """deserializes the JSON file to __objects otherwise, do nothing
         If the file doesn’t exist, no exception should be raised)"""

        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {k: self.classes()[v["__class__"]](**v)
                        for k, v in obj_dict.items()}
            FileStorage.__objects = obj_dict
