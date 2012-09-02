# -*- coding: utf-8 -*-

from framework import DoubanClientTestBase, main

class TestApiMovie(DoubanClientTestBase):
    def setUp(self):
        super(TestApiMovie, self).setUp()
        self.user_id = '40774605'


if __name__ == '__main__':
    main()
