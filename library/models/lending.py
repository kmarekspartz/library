"""
Defines the Lending model.
"""
from datetime import date
from sqlalchemy import Column, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship
from library import config
from library.models import Base, Book, Member

lending_period = date.fromtimestamp(float(config['LENDING_PERIOD']))


class Lending(Base):
    """
    The Lending model represents when a Member has checked out a Book.
    """
    __tablename__ = 'lendings'
    from_date = Column(Date, nullable=False)
    due_date = Column(Date, nullable=False)
    returned_date = Column(Date, nullable=True)  # This column can be null!

    book_id = Column(Integer, ForeignKey('books.id'))
    book = relationship(Book, primaryjoin=book_id == Book.id)

    member_id = Column(Integer, ForeignKey('members.id'))
    member = relationship(Member, primaryjoin=member_id == Member.id)

    @classmethod
    def lend_book_to_member(cls, book, member):
        """
        Constructs a lending from a book and a member.

        Sets the from- and due-dates.
        """
        lending = cls()
        lending.book_id = book.id
        lending.member_id = member.id
        lending.from_date = date.today()
        lending.due_date = date.today() + lending_period
        return lending

    def return_book(self):
        """
        End this lending.
        """
        assert self.returned_date is None
        self.returned_date = date.today()

    def relend(self):
        """
        Extend an existing lending with a new lending.
        """
        self.return_book()
        return type(self)().lend_book_to_member(self.book, self.member)
