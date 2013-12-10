from unittest import TestCase

from library.models.book import Book

from tests.unit.models.test_base import BaseTest


class TestBook(BaseTest, TestCase):
    cls = Book

    def test_class_has_title(self):
        """
        The Book model should have a relationship to a Title.
        """
        self.assertTrue(hasattr(self.cls, 'title_id'))
        self.assertTrue(hasattr(self.cls, 'title'))

    def test_instance_has_title(self):
        """
        Each Book instance should have a relationship to a Title.
        """
        self.assertTrue(hasattr(self.instance, 'title_id'))
        self.assertTrue(hasattr(self.instance, 'title'))

    def test_class_has_book_from_isbn(self):
        """
        The Book model should have a constructor which takes an ISBN.
        """
        self.assertTrue(hasattr(self.cls, 'book_from_isbn'))
