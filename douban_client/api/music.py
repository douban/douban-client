# -*- coding: utf-8 -*-

from .base import DoubanApiBase, DEFAULT_START, DEFAULT_COUNT

class Music(DoubanApiBase):

    def __repr__(self):
        return '<DoubanAPI Music>'
    """
    def get(self, id):
        return self._get('/v2/music/%s/'%id)

    def search(self, q=None, tag=None, start=DEFAULT_START, count=DEFAULT_COUNT):
        query = ''
        if q:
            query = q
        elif tag:
            query = tag
        return self._get('/v2/music/search', q=query, start=start, count=count)

    def reviews(self, id, start=DEFAULT_START, count=DEFAULT_COUNT):
        return self._get('/v2/music/%s/review'%id, start=start,count=count)

    def top_tags(self, id, start=DEFAULT_START, count=DEFAULT_COUNT):
        return self._get('/v2/music/%s/tags'%id, start=start, count=count)

    def review(self, id):
        return self._get('/v2/music/review/%s'%id)

    def create_review(self, music, title, content, rating=None):
        return self._post('/v2/music/reviews', music=music, title=title, content=content, rating=rating)

    def update_review(self, id, title, content, rating=None):
        return self._put('/v2/music/review/%s'%id, title=title, content=content, rating=rating)

    def delete_review(self, id):
        return self._delete('/v2/music/review/%s'%id)

    def all_tags(self, id, start=DEFAULT_START, count=DEFAULT_COUNT):
        return self._get('/v2/music/people_tags/%s'%id, start=start, count=count)
    """

