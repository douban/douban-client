# -*- coding: utf-8 -*-

from .user import User
from .doumail import Doumail
from .discussion import Discussion
from .note import Note
from .album import Album
from .photo import Photo
from .online import Online
from .event import Event
from .guess import Guess
from .miniblog import Miniblog
from .book import Book
from .movie import Movie
from .music import Music

class DoubanApi(object):

    def __repr__(self):
        return '<DoubanClient API>'

    @property
    def user(self):
        return User(self.access_token)

    @property
    def doumail(self):
        return Doumail(self.access_token)

    @property
    def discussion(self):
        return Discussion(self.access_token)

    @property
    def note(self):
        return Note(self.access_token)

    @property
    def album(self):
        return Album(self.access_token)

    @property
    def photo(self):
        return Photo(self.access_token)

    @property
    def online(self):
        return Online(self.access_token)

    @property
    def event(self):
        return Event(self.access_token)

    @property
    def guess(self):
        return Guess(self.access_token)

    @property
    def miniblog(self):
        return Miniblog(self.access_token)

    @property
    def book(self):
        return Book(self.access_token)

    @property
    def movie(self):
        return Movie(self.access_token)

    @property
    def music(self):
        return Music(self.access_token)
