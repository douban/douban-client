# -*- coding: utf-8 -*-

from .base import DoubanAPIBase


class Review(DoubanAPIBase):

    def __init__(self, access_token, target):
        self.access_token = access_token
        self.target = target

    def new(self, target_id, title, content, rating=''):
        data = {self.target: target_id,
                'title': title,
                'content': content,
                'rating': rating, }
        return self._post('/v2/%s/reviews' % self.target, **data)

    def update(self, id, title, content, rating=''):
        data = {self.target: id,
                'title': title,
                'content': content,
                'rating': rating, }
        return self._put('/v2/%s/review/%s' % (self.target, id), **data)

    def delete(self, id):
        return self._delete('/v2/%s/review/%s' % (self.target, id))
