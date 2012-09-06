# -*- coding: utf-8 -*-

from .subject import Subject

class Music(Subject):

    target = 'music'

    def __repr__(self):
        return '<DoubanAPI Music>'

