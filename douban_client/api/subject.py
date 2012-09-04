# -*- coding: utf-8 -*-

from .base import DoubanApiBase, DEFAULT_START, DEFAULT_COUNT
from .review import Review

class Subject(DoubanApiBase):

    cate = None

    def get(self, id):
        return self._get('/v2/%s/%s'%(self.cate, id))

    def reviews(self, id, start=DEFAULT_START, count=DEFAULT_COUNT):
        return self._get('/v2/%s/%s/reviews'%(self.cate, id), start=start, count=count)

    def search(self, q='', tag='', start=DEFAULT_START, count=DEFAULT_COUNT):
        return self._get('/v2/%s/search'%self.cate, q=q, tag=tag, start=start, count=count)

    def tags(self, id):
        return self._get('/v2/%s/%s/tags'%(self.cate, id))

    def tagged_list(self, id):
        return self._get('/v2/%s/people_tags/%s'%(self.cate, id))

    @property
    def review(self):
        return Review(self.client, self.cate)
