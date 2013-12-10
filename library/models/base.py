"""
Defines the Base model inherited by all models.
"""

from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.exc import ObjectDeletedError
from wtforms import Form
from wtforms.ext.sqlalchemy.orm import model_form
from library.models import Session


class LibraryBase(object):
    """
    Base class inherited by all models.

    Provides:
    - id column
    - cls.get_form method.
    """
    # Each model should have an id
    id = Column('id', Integer, primary_key=True)

    @classmethod
    def get_form(cls):
        """
        Returns a WTForm for the model class.

        Make sure to specify model.field_args for validators.

        See: http://flask.pocoo.org/snippets/60/
        """
        if hasattr(cls, 'field_args'):
            return model_form(cls, Form, field_args=cls.field_args)
        return model_form(cls, Form)

    @classmethod
    def get(cls, id):
        """
        Returns either the Instance with the given id, or None.
        """
        try:
            return Session.query(cls).get(id)
        except ObjectDeletedError:
            return None


Base = declarative_base(cls=LibraryBase)
