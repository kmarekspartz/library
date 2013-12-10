"""
Defines the Member models.
"""
from flask.ext.login import UserMixin
from sqlalchemy import Column, String

from library.models import Base


class AnonymousMember(object):
    """
    An unauthenticated user.

    Used for unauthenticated users with Flask-login.
    """
    pass


class Member(Base, UserMixin):
    """
    A member of the Library.

    Used with Flask-login.
    """
    __tablename__ = 'members'
    email = Column(String(255), nullable=False, unique=True)
    name = Column(String(255), nullable=False)
    password_hash = Column(String(1023), nullable=False)

    @classmethod
    def member_from_email_and_password(cls, email, password, name=None):
        """
        Construct a member from an email and a password.
        """
        member = cls()
        member.email = email
        member.set_password(password)
        if name:
            member.name = name
        else:
            member.name = email
        return member


    def set_password(self, password):
        """
        Set the password with bcrypt.
        """
        from library.app import bcrypt
        self.password_hash = bcrypt.generate_password_hash(password)

    def check_password(self, password):
        """
        Check the password with bcrypt.
        """
        from library.app import bcrypt
        return bcrypt.check_password_hash(self.password_hash, password)
