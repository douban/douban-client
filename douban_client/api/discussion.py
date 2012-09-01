# -*- coding: utf-8 -*-

from .base import DoubanApiBase, DEFAULT_START, DEFAULT_COUNT

class Discussion(DoubanApiBase):

    def __repr__(self):
        return '<DoubanAPI Discussion>'

    def get(self, id):
        return self._get('/v2/discussion/%s'%id)

    def update(self, id, title, content):
        return self._put('/v2/discussion/%s'%id, title=title, content=content)

    def delete(self, id):
        return self._delete('/v2/discussion/%S'%id)

    def new(self, target, id, title, content):
        return self._post('/v2/%s/%s/discussions'%(target, id), title=title, content=content)

    def gets(self, target, id):
        return self._get('/v2/%s/%s/discussions'%(target, id))
