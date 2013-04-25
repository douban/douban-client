# -*- coding: utf-8 -*-

from .base import DoubanApiBase, DEFAULT_START, DEFAULT_COUNT

class Online(DoubanApiBase):

    def __repr__(self):
        return '<DoubanAPI Online>'

    def get(self, id):
        return self._get('/v2/online/%s'%id)

    def new(self, title, desc, begin_time, end_time,
            related_url='', cascade_invite='false', tags=''):
        return self._post('/v2/onlines',
                title=title, desc=desc, begin_time=begin_time, end_time=end_time,
                related_url=related_url, cascade_invite=cascade_invite, tags=tags)

    def update(self, id, title, desc, begin_time, end_time,
            related_url='', cascade_invite='false', tags=''):
        return self._put('/v2/online/%s'%id,
                title=title, desc=desc, begin_time=begin_time, end_time=end_time,
                related_url=related_url, cascade_invite=cascade_invite, tags=tags)

    def delete(self, id):
        return self._delete('/v2/online/%s'%id)

    def join(self, id):
        return self._post('/v2/online/%s/participants'%id)

    def quit(self, id):
        return self._delete('/v2/online/%s/participants'%id)

    def photos(self, id, start=DEFAULT_START, count=DEFAULT_COUNT, order='', sortby='time'):
        return self._get('/v2/online/%s/photos'%id, start=start, count=count, order=order, sortby=sortby)

    def upload(self, id, image, desc=''):
        return self._post('/v2/online/%s/photos'%id, desc=desc, files={'image': image})

    def like(self, id):
        return self._post('/v2/online/%s/like'%id)

    def unlike(self, id):
        return self._delete('/v2/online/%s/like'%id)

    def participants(self, id, start=DEFAULT_START, count=DEFAULT_COUNT):
        return self._get('/v2/online/%s/participants'%id, start=start, count=count)

    def discussions(self, id, start=DEFAULT_START, count=DEFAULT_COUNT):
        return self._get('/v2/online/%s/discussions'%id, start=start, count=count)

    @property
    def discussion(self):
        return OnlineDiscussion(self.access_token)

    def list(self, cate='day', start=DEFAULT_START, count=DEFAULT_COUNT):
        # cate: day, week, latest
        return self._get('/v2/onlines', cate=cate, start=start, count=count)

    def created(self, user_id, start=DEFAULT_START, count=DEFAULT_COUNT):
        return self._get('/v2/online/user_created/%s'%user_id, start=start, count=count)

    def joined(self, user_id, start=DEFAULT_START, count=DEFAULT_COUNT):
        return self._get('/v2/online/user_participated/%s'%user_id, start=start, count=count)


class OnlineDiscussion(DoubanApiBase):

    def new(self, target_id, title, content):
        return self._post('/v2/online/%s/discussions'%target_id, title=title, content=content)
