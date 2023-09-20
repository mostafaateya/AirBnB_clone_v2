#!/usr/bin/python3
""" """
import os

from models.city import City
from tests.test_models.test_base_model import TestBasemodel


class TestState(TestBasemodel):
    """Test model for state"""

    def __init__(self, *args, **kwargs):
        """Initializes the test class."""
        super().__init__(*args, **kwargs)
        self.args = args
        self.kwargs = kwargs

    def testPlaceId(self):
        """Test [place id]"""
        new = self.value()
        self.assertEqual(
            type(new.place_id),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def TestUserID(self):
        """Test user """
        new = self.value()
        self.assertEqual(
            type(new.user_id),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def TestText(self):
        """Test text"""
        new = self.value()
        self.assertEqual(
            type(new.text),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )
