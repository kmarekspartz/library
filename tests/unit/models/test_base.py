"""
Defines the Base test for models.
"""
from library.models import Base


class BaseTest(object):
    """
    Base test for models.

    *NOTE:* This does not test the Base model, but instead is used to help
            write tests for the models.
    """
    cls = None
    instance = None

    def setUp(self):
        self.instance = self.cls()

    def test_class_issubclass_base(self):
        """
        Each model should inherit from issubclass.
        """
        self.assertTrue(issubclass(self.cls, Base))

    def test_class_has_id(self):
        """
        Each model should have an id column.
        """
        self.assertTrue(hasattr(self.cls, 'id'))
        ## It should be Integer
        ## It should be set to primary_key

    def test_instance_has_id(self):
        """
        Each model instance should have an id field.
        """
        self.assertTrue(hasattr(self.instance, 'id'))
        ## It should be int (after commit)
        ## It should not be None (after commit)

    def test_instance_isinstance_cls(self):
        """
        Each model instance should be an instance of its class.
        """
        self.assertIsInstance(self.instance, Base)
        self.assertIsInstance(self.instance, self.cls)

    def test_class_has_get(self):
        """
        Classes should have a get method.
        """
        self.assertTrue(hasattr(self.cls, 'get'))

    def test_class_has_get_form(self):
        """
        Classes should have a get_form method.
        """
        self.assertTrue(hasattr(self.cls, 'get_form'))


