# -*- coding: utf-8 -*-

from .base import DoubanApiBase, DEFAULT_START, DEFAULT_COUNT

class People(DoubanApiBase):

    def __repr__(self):
        return '<DoubanAPI People>'

    def get(self, id):
        return self._get('/v2/people/%s'%id)
    
    @property
    def me(self):
        return self.get('~me')

    def search(self, q='', start=DEFAULT_START, count=DEFAULT_COUNT):
        return self._get('/v2/people', q=q, start=start, count=count)

    def follow(self, id):
        return self._post('/shuo/friendships/create', user_id=id)

    def unfollow(self, id):
        return self._post('/shuo/friendships/destroy', user_id=id)

    def block(self, id):
        ret = self._post('/shuo/users/%s/block'%id)
        return ret['r'] == 1

    def friendships(self, target_id, source_id=''):
        return self._get('/shuo/friendships/show', target_id=target_id, source_id=source_id)

    def following(self, id, start=DEFAULT_START, count=DEFAULT_COUNT):
        page = start/count
        return self._get('/shuo/users/%s/following'%id, page=page, count=count)

    def followers(self, id, start=DEFAULT_START, count=DEFAULT_COUNT):
        page = start/count
        return self._get('/shuo/users/%s/followers'%id, page=page, count=count)

    def follow_in_common(self, id, start=DEFAULT_START, count=DEFAULT_COUNT):
        page = start/count
        return self._get('/shuo/users/%s/follow_in_common'%id, page=page, count=count)

    # def suggestions(self, id, start=DEFAULT_START, count=DEFAULT_COUNT):
    #     page = start/count
    #     return self._get('/shuo/users/%s/suggestions'%id, page=page, count=count)
