from unittest import TestCase

from library.models.title import Title

from tests.unit.models.test_base import BaseTest


class TestTitle(BaseTest, TestCase):
    cls = Title

    def test_class_has_isbn(self):
        """
        The Title model should have an ISBN.
        """
        self.assertTrue(hasattr(self.cls, 'isbn'))

    def test_instance_has_isbn(self):
        """
        Each Title should have an ISBN.
        """
        self.assertTrue(hasattr(self.instance, 'isbn'))

    def test_class_has_name(self):
        """
        The Title model should have a name.
        """
        self.assertTrue(hasattr(self.cls, 'name'))

    def test_instance_has_name(self):
        """
        Each Title should have a name.
        """
        self.assertTrue(hasattr(self.instance, 'name'))

    def test_class_has_title_from_isbn(self):
        """
        The Title model should have a constructor which takes an ISBN.
        """
        self.assertTrue(hasattr(self.cls, 'title_from_isbn'))
