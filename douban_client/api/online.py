# -*- coding: utf-8 -*-

from .base import DoubanApiBase, DEFAULT_START, DEFAULT_COUNT

class Online(DoubanApiBase):

    def __repr__(self):
        return '<DoubanAPI Online>'

    def get(self, id):
        return self._get('/v2/online/%s'%id)


