from unittest import TestCase

from library.models.lending import Lending

from tests.unit.models.test_base import BaseTest


class TestLending(BaseTest, TestCase):
    cls = Lending

    def test_class_has_book(self):
        """
        The Lending model should have a relationship with a Book.
        """
        self.assertTrue(hasattr(self.cls, 'book_id'))
        self.assertTrue(hasattr(self.cls, 'book'))

    def test_instance_has_book(self):
        """
        Each instance should have a relationship with a Book.
        """
        self.assertTrue(hasattr(self.instance, 'book_id'))
        self.assertTrue(hasattr(self.instance, 'book'))

    def test_class_has_member(self):
        """
        The Lending model should have a relationship with a Member.
        """
        self.assertTrue(hasattr(self.cls, 'member_id'))
        self.assertTrue(hasattr(self.cls, 'member'))

    def test_instance_has_member(self):
        """
        Each instance should have a relationship with a Book.
        """
        self.assertTrue(hasattr(self.instance, 'member_id'))
        self.assertTrue(hasattr(self.instance, 'member'))

    def test_class_has_from_date(self):
        """
        The Lending model should have a from date.
        """
        self.assertTrue(hasattr(self.cls, 'from_date'))

    def test_instance_has_from_date(self):
        """
        Each Lending should have a from date.
        """
        self.assertTrue(hasattr(self.instance, 'from_date'))

    def test_class_has_due_date(self):
        """
        The Lending model should have a due date.
        """
        self.assertTrue(hasattr(self.cls, 'due_date'))

    def test_instance_has_due_date(self):
        """
        Each Lending should have a due date.
        """
        self.assertTrue(hasattr(self.instance, 'due_date'))

    def test_class_has_returned_date(self):
        """
        The Lending model should have a returned date.
        """
        self.assertTrue(hasattr(self.cls, 'returned_date'))

    def test_instance_has_returned_date(self):
        """
        Each Lending should have a returned date.
        """
        self.assertTrue(hasattr(self.instance, 'returned_date'))

    def test_class_has_lend_book_to_member(self):
        """
        The Lending model should have a constructor which takes a book and a
        member.
        """
        self.assertTrue(hasattr(self.cls, 'lend_book_to_member'))

    def test_instance_has_return_book(self):
        """
        Each Lending should have a return book method.
        """
        self.assertTrue(hasattr(self.instance, 'return_book'))

    def test_instance_has_relend(self):
        """
        Each Lending should have a relend method.
        """
        self.assertTrue(hasattr(self.instance, 'relend'))
