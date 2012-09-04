# -*- coding: utf-8 -*-

from .base import DoubanApiBase, DEFAULT_START, DEFAULT_COUNT

class Book(DoubanApiBase):

    def __repr__(self):
        return '<DoubanAPI Book>'

    def get(self, id):
        return self._get('/v2/book/%s'%id)

