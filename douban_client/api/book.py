# -*- coding: utf-8 -*-

from .subject import Subject

class Book(Subject):

    target = 'book'

    def __repr__(self):
        return '<DoubanAPI Book>'

    def isbn(self, isbn_id):
        return self._get('/v2/book/isbn/%s'%isbn_id)
