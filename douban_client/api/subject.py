# -*- coding: utf-8 -*-

from .base import DoubanApiBase, DEFAULT_START, DEFAULT_COUNT
from .review import Review

class Subject(DoubanApiBase):

    target = None

    def get(self, id):
        return self._get('/v2/%s/%s'%(self.target, id))

    def search(self, q='', tag='', start=DEFAULT_START, count=DEFAULT_COUNT):
        return self._get('/v2/%s/search'%self.target, q=q, tag=tag, start=start, count=count)

    def tags(self, id):
        return self._get('/v2/%s/%s/tags'%(self.target, id))

    def tagged_list(self, id):
        return self._get('/v2/%s/user_tags/%s'%(self.target, id))

    # def reviews(self, id, start=DEFAULT_START, count=DEFAULT_COUNT):
    #     return Review(self.access_token, self.target).list(id, start=start, count=count)

    @property
    def review(self):
        return Review(self.access_token, self.target)
