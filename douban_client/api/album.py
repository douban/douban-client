# -*- coding: utf-8

from .base import DoubanApiBase, DEFAULT_START, DEFAULT_COUNT

class Album(DoubanApiBase):

    def __repr__(self):
        return '<DoubanAPI Album>'

    def get(self, id):
        return self._get('/v2/album/%s'%id)

    def new(self, title, desc='', order='desc', privacy='public'):
        return self._post('/v2/albums', title=title, desc=desc, order=order, privacy=privacy)

    def update(self, id, title='', desc='', order='desc', privacy='public'):
        return self._put('/v2/album/%s'%id, title=title, desc=desc, order=order, privacy=privacy)
    
    def delete(self, id):
        return self._delete('/v2/album/%s'%id)

    def list(self, user_id, start=DEFAULT_START, count=DEFAULT_COUNT):
        return self._get('/v2/album/user_created/%s'%user_id, start=start, count=count)

    def liked_list(self, user_id, start=DEFAULT_START, count=DEFAULT_COUNT):
        return self._get('/v2/album/user_liked/%s'%user_id, start=start, count=count)

    def photos(self, id, start=DEFAULT_START, count=DEFAULT_COUNT, order='', sortby='time'):
        return self._get('/v2/album/%s/photos'%id, start=start, count=count, order=order, sortby=sortby)

    def like(self, id):
        return self._post('/v2/album/%s/like'%id)

    def unlike(self, id):
        return self._delete('/v2/album/%s/like'%id)
