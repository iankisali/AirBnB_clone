#!/usr/bin/python3
"""Model creating User class"""

from models.base_model import BaseModel


class City(BaseModel):
    """class to manage city object"""
    state_id = ""
    name = ""
