#!/usr/bin/python3
"""
Unittes for DBStorage class
"""

from models.engine.db_storage import DBStorage
import os
import unittest


@unittest.skipIf(
    os.getenv("HBNB_TYPE_STORAGE") != "db",
    "requires DBStorage",
)
class test_DB_Storage(unittest.TestCase):
    """
    DBStorage tests
    """

    def test_documentation(self):
        """Documentation test"""
        self.assertIsNot(DBStorage.__doc__, None)
