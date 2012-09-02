# -*- coding: utf-8 -*-

from framework import DoubanClientTestBase, main

class TestApiBook(DoubanClientTestBase):
    def setUp(self):
        super(TestApiBook, self).setUp()
        self.user_id = '40774605'


if __name__ == '__main__':
    main()
