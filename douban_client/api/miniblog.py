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

    def rec(self, title='', url='', desc='', image=''):
        return self._post('/shuo/v2/statuses/', rec_title=title, rec_url=url, rec_desc=desc, rec_image=image)

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

    def reshareders(self, id):
        return self._get('/shuo/v2/statuses/%s/reshare'%id)

    def comments(self, id):
        return self._get('/shuo/v2/statuses/%s/comments'%id)

    @property
    def comment(self):
        return MiniblogComment(self.access_token)


class MiniblogComment(DoubanApiBase):

    def new(self, miniblog_id, text):
        return self._post('/shuo/v2/statuses/%s/comments'%miniblog_id, text=text)

    def get(self, id):
        return self._get('/shuo/v2/statuses/comment/%s'%id)

    def delete(self, id):
        return self._delete('/shuo/v2/statuses/comment/%s'%id)
