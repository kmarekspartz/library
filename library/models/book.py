"""
Defines the Book model.
"""
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from library.models import Base, Title


class Book(Base):
    """
    The Book model represents copies of Books.

    This is different from the Title model, which represents a book in the
    abstract. Books can be thought of as instances of their Titles.
    """
    __tablename__ = 'books'
    title_id = Column(Integer, ForeignKey('titles.id'))
    title = relationship(Title, primaryjoin=title_id == Title.id)

    @classmethod
    def book_from_isbn(cls, isbn):
        """
        Construct a new book from an ISBN.
        """
        book = cls()
        book.title = Title.title_from_isbn(isbn)
        return book
