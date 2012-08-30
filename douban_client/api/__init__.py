# -*- coding: utf-8 -*-

from .people import People
from .doumail import Doumail
from .discussion import Discussion
from .note import Note
from .album import Album
from .photo import Photo
from .online import Online
from .event import Event
from .guess import Guess
from .miniblog import Miniblog

class DoubanApi(object):

    def __repr__(self):
        return '<DoubanClient API>'

    @property
    def people(self):
        return People(self.client)

    @property
    def doumail(self):
        return Doumail(self.client)

    @property
    def discussion(self):
        return Discussion(self.client)

    @property
    def note(self):
        return Note(self.client)

    @property
    def album(self):
        return Album(self.client)

    @property
    def photo(self):
        return Photo(self.client)

    @property
    def online(self):
        return Online(self.client)

    @property
    def event(self):
        return Event(self.client)

    @property
    def guess(self):
        return Guess(self.client)

    @property
    def miniblog(self):
        return Miniblog(self.client)
