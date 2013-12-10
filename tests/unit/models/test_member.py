from unittest import TestCase
from flask.ext.login import UserMixin

from library.models.member import Member

# *NOTE:* AnonymousMember is a pseudo-model, so it does not pass these tests.

from tests.unit.models.test_base import BaseTest


class TestMember(BaseTest, TestCase):
    cls = Member

    def test_class_has_email(self):
        """
        The Member model should have an email.
        """
        self.assertTrue(hasattr(self.cls, 'email'))

    def test_instance_has_email(self):
        """
        Each Member should have an email.
        """
        self.assertTrue(hasattr(self.instance, 'email'))

    def test_class_has_password_hash(self):
        """
        The Member model should have a password hash.
        """
        self.assertTrue(hasattr(self.cls, 'password_hash'))

    def test_instance_has_password_hash(self):
        """
        Each Member should have a password hash.
        """
        self.assertTrue(hasattr(self.instance, 'password_hash'))

    def test_class_has_name(self):
        """
        The Member model should have a name.
        """
        self.assertTrue(hasattr(self.cls, 'name'))

    def test_instance_has_name(self):
        """
        Each Member should have a name.
        """
        self.assertTrue(hasattr(self.instance, 'name'))

    def test_class_issubclass_user_mixin(self):
        """
        The Member model should inherit UserMixin from Flask-Login.
        """
        self.assertTrue(issubclass(self.cls, UserMixin))
        self.assertTrue(hasattr(self.cls, 'is_authenticated'))
        self.assertTrue(hasattr(self.cls, 'is_active'))
        self.assertTrue(hasattr(self.cls, 'is_anonymous'))
        self.assertTrue(hasattr(self.cls, 'get_id'))

    def test_instance_isintance_user_mixin(self):
        """
        Each Member should be an instance of UserMixin from Flask-Login.
        """
        self.assertIsInstance(self.instance, UserMixin)
        self.assertTrue(hasattr(self.instance, 'is_authenticated'))
        self.assertTrue(hasattr(self.instance, 'is_active'))
        self.assertTrue(hasattr(self.instance, 'is_anonymous'))
        self.assertTrue(hasattr(self.instance, 'get_id'))

    def test_instance_has_set_password(self):
        """
        Each Member should have a set_password method.
        """
        self.assertTrue(hasattr(self.instance, 'set_password'))

    def test_instance_has_check_password(self):
        """
        Each Member should have a check_password method.
        """
        self.assertTrue(hasattr(self.instance, 'check_password'))

    def test_class_has_member_from_email_and_password(self):
        """
        The Member class should has a constructor which takes an email and a
        password.
        """
        self.assertTrue(hasattr(self.cls, 'member_from_email_and_password'))

