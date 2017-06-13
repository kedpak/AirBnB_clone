#!/usr/bin/python3

from models.base_model import BaseModel


class Review(BaseModel):
    """ public instance attribute: Review
    """
    place_id = ""
    user_id = ""
    text = ""
