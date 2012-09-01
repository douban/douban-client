# -*- coding: utf-8 -*-

from .base import DoubanApiBase, DEFAULT_START, DEFAULT_COUNT

class Miniblog(DoubanApiBase):

    def __repr__(self):
        return '<DoubanAPI Miniblog>'

    def get(self, id):
        return self._get('/shuo/v2/statuses/%s'%id)

    def new(self, text, image=None):
        files = dict(image=image) if image else dict()
        return self._post('/shuo/v2/statuses/', text=text, files=files)

    def delete(self, id):
        return self._delete('/shuo/v2/statuses/%s'%id)

    def home_timeline(self, count=DEFAULT_COUNT, since_id=None, until_id=None, category=None):
        return self._get('/shuo/v2/statuses/home_timeline', count=count, since_id=since_id, until_id=until_id, category=category)

    def user_timeline(self, user_id, since_id=None, until_id=None):
        return self._get('/shuo/v2/statuses/user_timeline/%s'%user_id, since_id=since_id, until_id=until_id)

    def mentions(self, count=DEFAULT_COUNT, since_id=None, until_id=None):
        return self._get('/shuo/v2/statuses/mentions', count=count, since_id=since_id, until_id=until_id)

    def like(self, id):
        return self._post('/shuo/v2/statuses/%s/like'%id)

    def unlike(self, id):
        return self._delete('/shuo/v2/statuses/%s/like'%id)

    def likers(self, id):
        return self._get('/shuo/v2/statuses/%s/like'%id)

    def reshare(self, id):
        return self._post('/shuo/v2/statuses/%s/reshare'%id)

    def unreshare(self, id):
        return self._delete('/shuo/v2/statuses/%s/reshare'%id)

    def resharers(self, id):
        return self._get('/shuo/v2/statuses/%s/reshare'%id)

    def comments(self, id):
        return self._get('/shuo/v2/statuses/%s/commetns'%id)

    def comment(self, text):
        return self._post('/shuo/v2/statuses/%s/commetns'%id)
