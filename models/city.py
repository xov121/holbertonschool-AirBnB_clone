#!/usr/bin/python3
from models.base_model import BaseModel


class City(BaseModel):
    """Represents a city with a state ID and name"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes City instance."""
        super().__init__(*args, **kwargs)
        self.state_id = kwargs.get('state_id', "")
        self.name = kwargs.get('name', "")
