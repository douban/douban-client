# -*- coding: utf-8 -*-

from .base import DoubanApiBase, DEFAULT_START, DEFAULT_COUNT

class Review(DoubanApiBase):

    def __init__(self, access_token, target):
        self.access_token = access_token
        self.target = target

    # def get(self, id):
    #     return self._get('/v2/%s/review/%s'%(self.cate, id))

    # def list(self, target_id, start=DEFAULT_START, count=DEFAULT_COUNT):
    #     return self._get('/v2/%s/%s/reviews'%(self.target, target_id), start=start, count=count)


    def new(self, target_id, title, content, rating=''):
        data = { self.target: target_id,
                 'title': title,
                 'content': content,
                 'rating': rating, }
        return self._post('/v2/%s/reviews'%self.target, **data)

    def update(self, id, title, content, rating=''):
        data = { self.target: id,
                 'title': title,
                 'content': content,
                 'rating': rating, }
        return self._put('/v2/%s/review/%s'%(self.target, id), **data)


    def delete(self, id):
        return self._delete('/v2/%s/review/%s'%(self.target, id))

