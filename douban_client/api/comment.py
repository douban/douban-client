# -*- coding: utf-8 -*-

from .base import DoubanApiBase, DEFAULT_START, DEFAULT_COUNT

class Comment(DoubanApiBase):

    def __init__(self, access_token, target):
        self.access_token = access_token
        self.target = target

    def __repr__(self):
        return '<DoubanAPI Comment>'

    def list(self, target_id, start=DEFAULT_START, count=DEFAULT_COUNT):
        return self._get('/v2/%s/%s/comments'%(self.target, target_id), start=start, count=count)

    def new(self, target_id, content):
        return self._post('/v2/%s/%s/comments'%(self.target, target_id), content=content)

    def get(self, target_id, id):
        return self._get('/v2/%s/%s/comment/%s'%(self.target, target_id, id))

    def delete(self, target_id, id):
        return self._delete('/v2/%s/%s/comment/%s'%(self.target, target_id, id))
