#!/usr/bin/python3
"""module creating review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class managing review"""
    place_id = ""
    user_id = ""
    text = ""
