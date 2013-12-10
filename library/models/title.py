"""
Defines the Title model.
"""
from sqlalchemy import String, Column
from sqlalchemy.orm.exc import NoResultFound

from library.models import Base, Session


class Title(Base):
    """
    The Title represents an abstract Book.

    This is opposed to the Book class. It represents a work an author has
    written, not a copy of that work.

    See: Type and Token distinction.
    """
    __tablename__ = 'titles'
    isbn = Column(String(255), nullable=False, unique=True)
    name = Column(String(255), nullable=False)

    @classmethod
    def title_from_isbn(cls, isbn, name=None):
        """
        Construct a title from an ISBN.
        """
        # Return an existing title if the ISBN is a duplicate.
        try:
            title = Session.query(cls).filter_by(isbn=isbn).one()
        except NoResultFound:
            # Construct a new title
            title = cls()
            title.isbn = isbn
            ## if not name:
                ## name_from_isbn(isbn) # Use an API
            title.name = name
        return title




