# -*- coding: utf-8 -*-

from .base import DoubanApiBase, DEFAULT_START, DEFAULT_COUNT

class Review(DoubanApiBase):

    def __init__(self, client, cate):
        self.client = client
        self.cate = cate

    def get(self, id):
        return self._get('/v2/%s/review/%s'%(self.cate, id)) 

    def new(self, id, title, content, rating=''):
        data = { self.cate: id,
                 'title': title,
                 'content': content,
                 'rating': rating, }
        return self._post('/v2/%s/reviews'%self.cate, **data)

    def update(self, id, title, content, rating=''):
        data = { self.cate: id,
                 'title': title,
                 'content': content,
                 'rating': rating, }
        return self._put('/v2/%s/review/%s'%(self.cate, id), **data)


    def delete(self, id):
        return self._delete('/v2/%s/review/%s'%(self.cate, id))

