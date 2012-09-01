# -*- coding: utf-8 -*-

from .base import DoubanApiBase, DEFAULT_START, DEFAULT_COUNT

class Comment(DoubanApiBase):

    def __repr__(self):
        return '<DoubanAPI Comment>'

    def list(self, target, target_id, start=DEFAULT_START, count=DEFAULT_COUNT):
        return self._get('/v2/%s/%s/comments'%(target, target_id), start=start, count=count)

    def new(self, target, target_id, content):
        return self._post('/v2/%s/%s/comments'%(target, target_id), content=content)

    def get(self, target, target_id, id):
        return self._get('/v2/%s/%s/comment/%s'%(target, target_id, id))

    def delete(self, target, target_id, id):
        return self._delete('/v2/%s/%s/comment/%s'%(target, target_id, id))
