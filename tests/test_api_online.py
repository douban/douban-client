# -*- coding: utf-8 -*-

from framework import DoubanClientTestBase, main

class TestApiOnline(DoubanClientTestBase):
    def setUp(self):
        super(TestApiOnline, self).setUp()
        self.user_id = '40774605'
        self.online_id = '11182611'

    def test_get_online(self):
        ret = self.client.online.get(self.online_id)
        print ret


if __name__ == '__main__':
    main()
