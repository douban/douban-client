# -*- coding: utf-8 -*-

from .base import DoubanApiBase, DEFAULT_START, DEFAULT_COUNT

class Event(DoubanApiBase):

    def __repr__(self):
        return '<DoubanAPI Event>'

    def get(self, id):
        return self._get('/v2/event/%s'%id)

    def list(self, loc, day_type=None, type=None, start=DEFAULT_START, count=DEFAULT_COUNT):
        return self._get('/v2/event/list', 
                loc=loc, day_type=day_type, type=type, start=start, count=count)

    def search(self, q, loc, start=DEFAULT_START, count=DEFAULT_COUNT):
        return self._get('/v2/event/search', q=q, loc=loc)

    def join(self, id, participate_date=''):
        data = dict(participate_date=participate_date) if participate_date else {}
        return self._post('/v2/event/%s/participants'%id, **data)

    def quit(self, id, participate_date=''):
        data = dict(participate_date=participate_date) if participate_date else {}
        return self._delete('/v2/event/%s/participants'%id, **data)

    def wish(self, id):
        return self._post('/v2/event/%s/wishers'%id)

    def unwish(self, id):
        return self._delete('/v2/event/%s/wishers'%id)

    def participants(self, id, start=DEFAULT_START, count=DEFAULT_COUNT):
        return self._get('/v2/event/%s/participants'%id, start=start, count=count)

    def wishers(self, id, start=DEFAULT_START, count=DEFAULT_COUNT):
        return self._get('/v2/event/%s/wishers'%id, start=start, count=count)

    def owned(self, user_id, start=DEFAULT_START, count=DEFAULT_COUNT):
        return self._get('/v2/event/user_created/%s'%user_id, start=start, count=count)

    def participated(self, user_id, start=DEFAULT_START, count=DEFAULT_COUNT):
        return self._get('/v2/event/user_participated/%s'%user_id, start=start, count=count)

    def wished(self, user_id, start=DEFAULT_START, count=DEFAULT_COUNT):
        return self._get('/v2/event/user_wished/%s'%user_id, start=start, count=count)

