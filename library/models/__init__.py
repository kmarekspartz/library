"""
Gathers the models into a module.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from library import config

engine = create_engine(config['SQLALCHEMY_DATABASE_URI'])
Session = scoped_session(sessionmaker(bind=engine))

from library.models.base import Base
from library.models.title import Title
from library.models.book import Book
from library.models.member import AnonymousMember, Member
from library.models.lending import Lending

Base.metadata.create_all(engine)


