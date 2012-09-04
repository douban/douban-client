# -*- coding: utf-8 -*-

from .subject import Subject

class Movie(Subject):

    cate = 'movie'

    def __repr__(self):
        return '<DoubanAPI Movie>'

    def imdb(self, imdb_id):
        return self._get('/v2/movie/imdb/%s'%imdb_id)
